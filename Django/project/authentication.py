from rest_framework.authentication import BaseAuthentication
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from core.settings import JWT_SECRET
import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

# 分別做為request.user跟request.auth(這個是根據方法決定用途的，這個範例裡是userToken)


class CustomAuth(BaseAuthentication):
    def authenticate(self, request: Request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("請先登入")
        # user_token = UserToken.objects.filter(userToken=token).first()
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms="HS256")
        except InvalidSignatureError:
            raise AuthenticationFailed("簽章驗證失敗")
        except ExpiredSignatureError:
            raise AuthenticationFailed("登入資訊過期，請重新登入")
        except Exception as e:
            print(e)
            raise AuthenticationFailed("未知錯誤發生")
        try:
            user = User.objects.get(pk=payload.get('user_email'))
        except User.DoesNotExist:
            user =  None
            token = ""
            raise AuthenticationFailed("使用者不存在")

        return user, token
