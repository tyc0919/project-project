from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from project.authentication import CustomAuth

from . import serializers
from .models import User, Collaborator, Activity, JobDetail, Job
from . import modules

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt


class CSRFEndpoint(APIView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request: Request):
        return Response({'success': 'CSRF cookie set!'})


class SignIn(APIView):
    parser_classes = [JSONParser]

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            user = modules.custom_login(request.data.get(
                "user_email"), request.data.get("password"))
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # 如果要傳入多個物件必須用many=True，然後可以丟整個QuerySet進去
        if not user:
            return Response(
                {
                    'error': '帳號或密碼有誤',
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = UserSerializer(user)
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
        serializer = serializers.UserProfileSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':'變更成功!'})

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

class GetBudget(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def get(self, request: Request, activity_id):
        try:
            activity = Activity.objects.get(pk=activity_id)
            budget = activity.activity_budget
        except:
            return Response({'error':'無此活動'},status=status.HTTP_404_NOT_FOUND)
        jobs = Job.objects.filter(activity=activity)
        expenditure = 0
        # wait for model revise to calculate expenditure and get files



class TestView(APIView):
    authentication_classes = [CustomAuth]
    @method_decorator(csrf_protect)
    def post(self, request):
        return Response({'success': 'Access is granted'})

