from rest_framework.authentication import BaseAuthentication
from .models import  User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
#有typo但我懶得改，authenticate方法需要return兩個東西
#分別做為request.user跟request.auth(這個是根據方法決定用途的，這個範例裡是userToken)
class CustomAuth(BaseAuthentication):
    def authenticate(self, request: Request):
        token = request.COOKIES.get('token')
        user_token = UserToken.objects.filter(userToken=token).first()
        if not user_token:
            raise AuthenticationFailed("請先登入")
        return user_token.user, token