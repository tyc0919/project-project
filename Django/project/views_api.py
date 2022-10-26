from django.http import FileResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
import uuid
import os
import datetime

from project.authentication import CustomAuth
from project.permissions import IsOwner
from project import modules, serializers

from .models import *

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt

# -----CSRF START------


class CSRFEndpoint(APIView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request: Request):
        return Response({'success': 'CSRF cookie set!'})

# -----CSRF END-----

# -----Authentication START-----


class SignIn(APIView):
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            user = modules.custom_login(request.data.get(
                "user_email"), request.data.get("password"))
        except Exception as e:
            print(Exception, ': ', e)
            return Response({'error': '缺少輸入資料'}, status=status.HTTP_400_BAD_REQUEST)

        # 如果要傳入多個物件必須用many=True，然後可以丟整個QuerySet進去
        if not user:
            return Response(
                {
                    'error': '帳號或密碼有誤',
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        response = Response({'success': '登入成功'})

        # response = Response({'msg': 'set cookie test'})
        response = modules.set_credential(response=response, user=user)
        return response


class SignUp(APIView):
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        if request.data.get('user_type') == "shop":
            return Response({'error': '尚未開放店家註冊!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            modules.register(request.data.get("user_email"),
                             request.data.get("password"),
                             request.data.get("user_name"))
            return Response({'success': '註冊成功!'})
        except ValidationError:
            data = {'error': 'Email格式輸入錯誤'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            data = {'error': '該Email已經被註冊'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {'error': '欄位不能為空', 'e': str(e)}
            print(Exception)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

# -----Authentication END-----

# -----UserProfile START-----


class GetUserProfile(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request):
        return Response(serializers.UserSerializer(request.user).data)


class UpdateUserProfile(APIView):
    parser_classes = [JSONParser]
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.UserProfileSerializer(
            request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': '變更成功!'})


class UpdateUserPassword(APIView):
    parser_classes = [JSONParser]
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        password = request.data.get('password')
        validated_data = serializers.UserPasswordSerializer(
            request.user, data={'password': password})  # use serializer to check field format

        validated_data.is_valid(raise_exception=True)
        if modules.check_password(password, request.user.password):
            new_password = request.data.get('new_password')
            validated_data = serializers.UserPasswordSerializer(
                request.user, data={'password': new_password})
            validated_data.is_valid(raise_exception=True)
            validated_data.save()
        else:
            return Response({'error': '密碼驗證失敗!'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'success': '變更成功'})

# -----UserProfile END-----
# -----Activity START-----


class GetActivityCards(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request):
        queryset = Collaborator.objects.filter(user_email=request.user)
        cards = []
        for as_collab in queryset:
            jobs = Job.objects.filter(activity=as_collab.activity)
            expenditure = 0
            for job in jobs:
                expenditure += job.job_expenditure
            data = dict(serializers.ActivityCardsSerializer(as_collab.activity).data) | {
                'activity_expenditure': expenditure}
            cards.append(data)
        return Response(cards)


class GetActivity(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            data = dict(serializers.ActivitySerializer(activity).data) | {'user_name': activity.owner.user_name}
        except:
            return Response({'error': '無此活動'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)


class CreateActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.ActivityUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': '新增成功'})


class UpdateActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request, activity)

        serializer = serializers.ActivityUpdateSerializer(
            activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        modules.event_logger(activity=activity, user=request.user,
                             msg=f"更新了活動資料，活動標題: '{request.data.get('activity_name')}'，活動敘述: {request.data.get('activity_description')}")
        return Response({'success': '更新成功'})


class UpdateActivityBudget(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request, activity)
        budget = activity.activity_budget

        serializer = serializers.ActivityBudgetSerializer(
            activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        modules.event_logger(activity=activity, user=request.user,
                             msg=f"更新了活動預算，由: {budget}，變更至: {request.data.get('activity_budget')}")
        return Response({'success': '更新成功'})


class DeleteActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request, activity)

        activity.delete()
        return Response({'success': '刪除成功'})


class PublishActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request, activity)

        serializer = serializers.ActivityPublishSerializer(
            activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        msg = '' if instance.is_public == 1 else '不'
        modules.event_logger(
            activity=activity, user=request.user, msg=f"將活動設置為公開")
        return Response({'success': f'已經將活動設置成{msg}公開!'})


class FinishActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request, activity)
        serializer = serializers.ActivityFinishSerializer(
            activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        msg = '' if instance.is_finished == 1 else '未'
        modules.event_logger(
            activity=activity, user=request.user, msg=f"將活動設置為完成")
        return Response({'success': f'已經將活動設置成{msg}完成!'})


class GetCollaborator(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        queryset = Collaborator.objects.filter(activity=activity_id)
        user_list = [x.user_email for x in queryset]
        data = serializers.UserInfoSerializer(user_list, many=True).data
        return Response(data)


# -----Activity END-----
# -----Job START-----

class GetMyJob(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request):
        queryset = Job.objects.filter(person_in_charge_email=request.user)
        return Response(serializers.JobSerializer(queryset, many=True).data)


class GetJob(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        queryset = Job.objects.filter(activity=activity_id)
        return Response(serializers.JobSerializer(queryset, many=True).data)


class GetCertainJob(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id, job_id):
        try:
            queryset = Job.objects.get(pk=job_id)
        except:
            return Response({'error': '找不到該工作'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.JobSerializer(queryset).data)


class CreateJob(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.JobCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()

        modules.event_logger(activity=job.activity, user=request.user,
                             msg=f"創建工作: {job.title}, 工作ID: {job.id}")
        return Response({'success': '新增成功'})


class UpdateJob(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    def get_object(self, **kwargs):
        return get_object_or_404(Job, pk=kwargs.get('job_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        job = self.get_object(job_id=request.data.get("job_id"))
        serializer = serializers.JobUpdateSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()

        # TODO: See if it's required to expand length linit
        modules.event_logger(activity=job.activity, user=request.user,
                             msg=f"更新了工作{job.title}(工作ID: {job.id})")
        return Response({'success': '更新成功'})


class DeleteJob(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Job, pk=kwargs.get('job_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            job = self.get_object(job_id=request.data.get("job_id"))
            activity = job.activity
            job_id = job.id
            job_title = job.title
            # TODO: check permission
            job.delete()
        except Exception as e:
            return Response({'error': f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        modules.event_logger(activity=activity, user=request.user,
                             msg=f"刪除了工作{job_title}(工作ID: {job_id})")
        return Response({'success': '刪除成功'})


class StatusJob(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Job, pk=kwargs.get('job_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        job = self.get_object(job_id=request.data.get("job_id"))
        serializer = serializers.JobStatusSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()
        result = '' if request.data.get("status") == 1 else '未'

        modules.event_logger(activity=job.activity, user=request.user,
                             msg=f"將工作{job.title}(工作ID: {job.id}的狀態設置為{result}完成)")
        return Response({'success': f'已將狀態設置為{result}完成'})


class GetJobDetail(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, job_id, activity_id):
        queryset = JobDetail.objects.filter(job_id=job_id)
        return Response(serializers.JobDetailSerializer(queryset, many=True).data)


class CreateJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.JobDetailCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        jd = serializer.save()

        modules.event_logger(activity=jd.activity, user=request.user,
                             msg=f"為工作{jd.job.title}(工作ID: {jd.job.id}新增工作細項: {jd.title}(細項ID:{jd.job_detail_id}))")
        return Response({'success': '新增成功'})


class DeleteJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(JobDetail, pk=kwargs.get('job_detail_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        jd = self.get_object(job_detail_id=request.data.get('job_detail_id'))
        activity = jd.activity
        title = jd.title
        jd_id = jd.job_detail_id
        # self.check_object_permissions(request,activity)
        jd.delete()

        modules.event_logger(activity=activity, user=request.user,
                             msg=f"將工作細項{title}(細項ID: {jd_id}刪除)")
        return Response({'success': '刪除成功'})


class UpdateJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(JobDetail, pk=kwargs.get('job_detail_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        jd = self.get_object(job_detail_id=request.data.get('job_detail_id'))
        # self.check_object_permissions(request,activity)

        serializer = serializers.JobDetailUpdateSerializer(
            jd, data=request.data)
        serializer.is_valid(raise_exception=True)
        jd = serializer.save()

        modules.event_logger(activity=jd.activity, user=request.user,
                             msg=f"更新了工作細項: {jd.title}(細項ID:{jd.job_detail_id})")
        return Response({'success': '更新成功'})


class StatusJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(JobDetail, pk=kwargs.get('job_detail_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        jd = self.get_object(job_detail_id=request.data.get('job_detail_id'))
        # self.check_object_permissions(request,activity)

        serializer = serializers.JobDetailStatusSerializer(
            jd, data=request.data)
        serializer.is_valid(raise_exception=True)
        jd = serializer.save()

        result = '' if request.data.get("status") == 1 else '未'
        modules.event_logger(activity=jd.activity, user=request.user,
                             msg=f"將工作細項: {jd.title}(細項ID:{jd.job_detail_id})狀態設置為{result}完成")
        return Response({'success': '更新成功'})

# -----Job END-----
# -----Budget START-----


class GetBudget(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            budget = activity.activity_budget
            exps = serializers.ExpenditureSerializer(
                Expenditure.objects.filter(activity=activity), many=True).data
            jobs = serializers.JobSerializer(
                Job.objects.filter(activity=activity), many=True).data
            data = {
                'activity_budget': budget,
                'expenditures': exps,
                'jobs': jobs
            }

        except:
            return Response({'error': '無此活動'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)

# -----Budget END-----
# -----Social START-----


class GetSocial(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request):
        queryset = Activity.objects.filter(is_public=1)
        return Response(serializers.ActivitySerializer(queryset, many=True).data)


class GetPublicActivity(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            if activity.is_public != 1:
                raise Exception
            data = serializers.SocialSerializer(activity).data
        except:
            return Response({'error': '無此活動'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)


class GetReview(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id, is_public=1)
            review_set = Review.objects.filter(activity=activity)
            result = []
            for review in review_set:
                temp = {
                    "id": review.id,
                    "content": review.content,
                    "review_time": review.review_time,
                    "review_star": review.review_star,
                    "activity": review.activity_id,
                    "reviewer": review.reviewer.user_email,
                    "user_name": review.reviewer.user_name
                }
                result.append(temp)
            
            # data = serializers.ReviewSerializer(review_set, many=True).data
        except Exception as e:
            print(e)
            return Response({'error': '無此活動'}, status=status.HTTP_404_NOT_FOUND)
        return Response(result)


class PostReview(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            data = {
                'activity': Activity.objects.get(pk=request.data.get("activity_id"), is_public=1).id,
                'reviewer': User.objects.get(pk=request.data.get("user_email")).user_email,
                'content': request.data.get("content"),
                'review_time': timezone.now(),
                'review_star': request.data.get("review_star")
            }
        except:
            return Response({'error': '使用者或活動不存在'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

        return Response({'success': '評論發佈成功'})


class UpdateReview(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            review = Review.objects.get(
                pk=request.data.get("id"), reviewer=request.user)
            data = {
                'content': request.data.get("content"),
                'review_star': request.data.get("review_star")
            }
        except Exception as e:
            print(str(e))
            return Response({'error': '使用者或活動不存在'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ReviewUpdateSerializer(review, data=data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

        return Response({'success': '評論修改成功'})


# -----Social END-----
# -----File START-----

class GetActivityFile(APIView):
    authentication_classes = [CustomAuth]

    def get_queryset(self, **kwargs):
        activity = get_object_or_404(Activity, pk=kwargs.get('activity_id'))
        return File.objects.filter(activity=activity)

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        queryset = self.get_queryset(activity_id=activity_id)
        # TODO: check permission then do below

        serializer = serializers.FileSerializer(queryset, many=True).data
        return Response(serializer)


class GetJobFile(APIView):
    authentication_classes = [CustomAuth]

    def get_queryset(self, **kwargs):
        job = get_object_or_404(Job, pk=kwargs.get('job_id'))
        return File.objects.filter(job=job)

    @method_decorator(csrf_protect)
    def get(self, request: Request, job_id):
        queryset = self.get_queryset(job_id=job_id)
        # TODO: check permission then do below

        serializer = serializers.FileSerializer(queryset, many=True).data
        return Response(serializer)


class UploadJobFile(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @method_decorator(csrf_protect)
    def post(self, request):
        try:
            job_id = int(request.data.get('job_id'))
            job = Job.objects.get(pk=job_id)
            # TODO: Check for permission then do below

            file = request.FILES['file']
            file_name = file.name
            fn_ext = file_name.rsplit(".")
            dupe = 0
            while File.objects.filter(file_path=file_name, activity=job.activity):
                dupe += 1
                ext = f".{fn_ext[-1]}" if len(fn_ext) > 1 else ""
                file_name = f'{fn_ext[0]}_{dupe}{ext}'
                print(file_name)

            with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name + f'_{job.activity_id}', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Add File info into database
            # TODO: Deal with repetitive file name
            new_file = File.objects.create(
                file_path=file_name,
                file_uploaded_time=timezone.now(),
                job=job,
                activity=job.activity
            )
            modules.event_logger(activity=new_file.activity, user=request.user,
                                 msg=f"上傳檔案: {file_name}至工作: {new_file.job}")
            return Response({'success': f'{file.name}檔案上傳成功'})
        except Exception as e:
            return Response({'error': '檔案上傳失敗', 'reason': e}, status=status.HTTP_400_BAD_REQUEST)


class UploadExpenditure(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @method_decorator(csrf_protect)
    def post(self, request):
        try:
            job_id = int(request.data.get('job_id'))
            expense = int(request.data.get('expense'))

            job = Job.objects.get(pk=job_id)
            # TODO: Check for permission then do below

            # The file name confliction solution is here
            file = request.FILES['file']
            file_name = file.name
            fn_ext = file_name.rsplit(".")
            dupe = 0
            while Expenditure.objects.filter(expenditure_receipt_path=file_name, activity=job.activity):
                dupe += 1
                ext = f".{fn_ext[-1]}" if len(fn_ext) > 1 else ""
                file_name = f'{fn_ext[0]}_{dupe}{ext}'
                print(file_name)

            with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name + f'_{job.activity_id}', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Add Expenditure info into database
            # TODO: Deal with repetitive file name to prevent file from overriden
            new_file = Expenditure.objects.create(
                expenditure_receipt_path=file_name,
                expenditure_uploaded_time=timezone.now(),
                job=job,
                activity=job.activity,
                expense=expense
            )
            sum_ex = 0
            all_receipt = Expenditure.objects.filter(job=job)
            for receipt in all_receipt:
                sum_ex += receipt.expense
            job.job_expenditure = sum_ex
            job.save()

            modules.event_logger(activity=new_file.activity, user=request.user,
                                 msg=f"上傳收據: {file_name}至工作: {new_file.job}")
            return Response({'success': f'{file.name}檔案上傳成功'})
        except Exception as e:
            return Response({'error': '檔案上傳失敗', 'reason': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


class UploadActivityPic(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @method_decorator(csrf_protect)
    def post(self, request):
        try:
            a_id = int(request.data.get('activity_id'))
            a = Activity.objects.get(pk=a_id)
            # TODO: Check for permission then do below

            file = request.FILES['file']
            file_name = uuid.uuid4().hex[:16] + ".jpg"
            with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Add Expenditure info into database
            # TODO: Deal with repetitive file name to prevent file from overriden
            a.activity_picture = file_name
            a.save()

            modules.event_logger(
                activity=a, user=request.user, msg=f"為活動上傳了新圖片")
            return Response({'success': f'{file.name}檔案上傳成功'})
        except:
            return Response({'error': '檔案上傳失敗'}, status=status.HTTP_400_BAD_REQUEST)


class UploadUserAvatar(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @method_decorator(csrf_protect)
    def post(self, request):
        try:
            user = request.user
            # TODO: Check for permission then do below
            #   Deal with arbitrary file upload

            file = request.FILES['file']
            file_name = uuid.uuid4().hex[:16] + ".jpg"
            with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            user.picture_path = file_name
            user.save()
            return Response({'success': '頭像上傳成功'})
        except Exception as e:
            print(e)
            return Response({'error': '檔案上傳失敗'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteFile(APIView):  # asdasd
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request):
        model = request.data.get("model")
        job_id = request.data.get("job_id")
        file_name = request.data.get("file_name")

        try:
            job = Job.objects.get(pk=job_id)
            local_path = os.path.join(settings.BASE_DIR).replace(
                '\\', '/') + '/project/static/project/avatar/' + file_name + f'_{job.activity_id}'
        except TypeError:
            return Response({'error': '請輸入檔案名稱'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '找不到該工作'}, status=status.HTTP_400_BAD_REQUEST)

        if model == "file":  # need activity id & job serial number
            try:
                f = File.objects.get(job=job, file_path=file_name)
                if os.path.exists(local_path):
                    modules.event_logger(
                        activity=f.activity, user=request.user, msg=f"刪除了檔案: {f.file_path}")
                    f.delete()
                    os.remove(local_path)
                    return Response({'success': '檔案已經刪除!'})
                return Response({'error': '檔案不存在'})
            except Exception as e:
                return Response({'error': '找不到該檔案', 'msg': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        elif model == "expenditure":
            try:
                f = Expenditure.objects.get(
                    job=job, expenditure_receipt_path=file_name)
                if os.path.exists(local_path):
                    modules.event_logger(
                        activity=f.activity, user=request.user, msg=f"刪除了檔案: {f.expenditure_receipt_path}")
                    f.delete()
                    os.remove(local_path)
                    return Response({'success': '檔案已經刪除!'})
                return Response({'error': '檔案不存在'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': '找不到該檔案', 'msg': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'model參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)


class ServeFile(APIView):
    authentication_classes = [CustomAuth]

    def get_object(self, **kwargs):
        activity = get_object_or_404(Activity, pk=kwargs.get('activity_id'))
        return activity

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id, file_name):
        activity = self.get_object(activity_id=activity_id)
        work_files = File.objects.filter(
            file_path=file_name, activity=activity)
        exp_files = Expenditure.objects.filter(
            expenditure_receipt_path=file_name, activity=activity)
        if (not work_files) and (not exp_files):
            raise Http404

        # TODO: check permission then do below
        try:
            f = open(os.path.join(settings.BASE_DIR).replace(
                '\\', '/') + '/project/static/project/avatar/' + file_name + f'_{activity_id}', 'rb')
        except:
            return Response({'error': '找不到檔案'}, status=status.HTTP_400_BAD_REQUEST)
        return FileResponse(f, filename=file_name)


class ServeAvatar(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, picture_path):
        try:
            f = open(os.path.join(settings.BASE_DIR).replace('\\', '/') +
                     '/project/static/project/avatar/' + picture_path, 'rb')
        except:
            return Response({'error': '找不到檔案'}, status=status.HTTP_400_BAD_REQUEST)
        return FileResponse(f)


class ServeActivityPic(APIView):
    authentication_classes = [CustomAuth]

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_picture):
        try:
            f = open(os.path.join(settings.BASE_DIR).replace('\\', '/') +
                     '/project/static/project/avatar/' + activity_picture, 'rb')
        except:
            return Response({'error': '找不到檔案'}, status=status.HTTP_400_BAD_REQUEST)
        return FileResponse(f)


# -----File END-----

# -----Log START-----
class GetLog(APIView):
    authentication_classes = [CustomAuth]

    def get_queryset(self, **kwargs):
        activity = get_object_or_404(Activity, pk=kwargs.get('activity_id'))
        return Log.objects.filter(activity=activity)

    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        queryset = self.get_queryset(activity_id=activity_id)
        # TODO: check permission then do below
        result_list = []
        for log in queryset:
            data = {
                "id": log.id,
                "user_email": log.user_email.user_email,
                "user_name": log.user_email.user_name,
                "action": log.action,
                "time": log.time
            }
            result_list.append(data)
        return Response(result_list)
# -----Log END-----


class TestView(APIView):
    # authentication_classes = [CustomAuth]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    # @method_decorator(csrf_protect)
    def post(self, request):
        try:
            # job_id = int(request.data.get('job_id'))
            # job = Job.objects.get(pk=job_id)

            # check for job permission then do below

            # file = request.FILES['file']

            # file_name = file.name
            # with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name , 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            # new_file = File.objects.create(
            #     file_path=file_name,
            #     file_uploaded_time=datetime.datetime.now(),
            #     job=job,
            #     activity=job.activity
            # )

            return Response({'success': '1'})
        except:
            return Response({'error': '2'}, status=status.HTTP_400_BAD_REQUEST)
