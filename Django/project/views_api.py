from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

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
        if request.data.get('user_type') == "shop": return Response({'error': '尚未開放店家註冊!'}, status=status.HTTP_400_BAD_REQUEST)
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
        print(password)
        validated_data = serializers.UserPasswordSerializer(
            request.user, data={'password': password})  # use serializer to check field format

        validated_data.is_valid(raise_exception=True)
        if modules.check_password(password,request.user.password):
            new_password = request.data.get('new_password')
            validated_data = serializers.UserPasswordSerializer(request.user, data={'password': new_password})
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
            cards.append(serializers.ActivityCardsSerializer(as_collab.activity).data)
        return Response(cards)

class GetActivity(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            data = serializers.ActivitySerializer(activity).data
        except:
            return Response({'error':'無此活動'},status=status.HTTP_404_NOT_FOUND)
        return Response(data)

class CreateActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.ActivityUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':'新增成功'})

class UpdateActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request,activity)

        serializer = serializers.ActivityUpdateSerializer(activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':'更新成功'})

class UpdateActivityBudget(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request,activity)

        serializer = serializers.ActivityBudgetSerializer(activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':'更新成功'})

class DeleteActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request,activity)

        activity.delete()
        return Response({'success':'刪除成功'})

class PublishActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request,activity)

        serializer = serializers.ActivityPublishSerializer(activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        msg = '' if instance.is_public == 1 else '不'
        return Response({'success':f'已經將活動設置成{msg}公開!'})

class FinishActivity(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(Activity, pk=kwargs.get('activity_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        activity = self.get_object(activity_id=request.data.get('activity_id'))
        self.check_object_permissions(request,activity)
        serializer = serializers.ActivityFinishSerializer(activity, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        msg = '' if instance.is_finished == 1 else '未'
        return Response({'success':f'已經將活動設置成{msg}完成!'})

class GetCollaborator(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        queryset = Collaborator.objects.filter(activity=activity_id)
        return Response(serializers.CollaboratorSerializer(queryset, many=True).data)


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
    
class GetJobDetail(APIView):                                                #job details below here are not finished
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def get(self, request: Request,job_serial_number, activity_id):
        queryset = JobDetail.objects.filter(job_serial_number=job_serial_number, activity=activity_id)
        return Response(serializers.JobDetailSerializer(queryset, many=True).data)

class CreateJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        serializer = serializers.JobDetailCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':'新增成功'})

class DeleteJobDetail(APIView):
    authentication_classes = [CustomAuth]
    parser_classes = [JSONParser]

    # permission_classes = [IsOwner]

    def get_object(self, **kwargs):
        return get_object_or_404(JobDetail, pk=kwargs.get('job_detail_id'))

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        jd = self.get_object(job_detail_id=request.data.get('job_detail_id'))
        # self.check_object_permissions(request,activity)
        jd.delete()
        return Response({'success':'刪除成功'})

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
        serializer = serializers.ActivityFinishSerializer(jd, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response({'success':'更新成功'})        

# -----Job END-----
# -----Budget START-----

class GetBudget(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            budget = activity.activity_budget
            exps =serializers.ExpenditureSerializer(Expenditure.objects.filter(activity=activity), many=True).data
            jobs =serializers.JobSerializer(Job.objects.filter(activity=activity), many=True).data
            data = {
                'activity_budget': budget,
                'expenditures': exps,
                'jobs': jobs
            }

        except:
            return Response({'error':'無此活動'},status=status.HTTP_404_NOT_FOUND)
        return Response(data)
        # wait for model revise to calculate expenditure and get files

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
            if activity.is_public != 1: raise Exception
            data = serializers.SocialSerializer(activity).data
        except:
            return Response({'error':'無此活動'},status=status.HTTP_404_NOT_FOUND)
        return Response(data)
# -----Social END-----

class TestView(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def post(self, request):
        return Response({'success': 'Access is granted'})

