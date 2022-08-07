from .modules import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from . import modules
import json

class LogIn(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({'msg': '資料為空'},status=status.HTTP_400_BAD_REQUEST)
        query = modules.custom_login(data.get("user_email"), data.get("password"))
        # 如果要傳入多個物件必須用many=True，然後可以丟整個QuerySet進去
        if not query: return Response({'msg': '帳號或密碼有誤', 'param1': data.get("user_email"),'param2': data.get("password")},status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(query)
        response = Response(serializer.data)
        
        # response = Response({'msg': 'set cookie test'})
        response.set_cookie('user', query.user_email, domain=".ace.project")
        return response