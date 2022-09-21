import hashlib
import uuid
import re
import jwt
import datetime


from core.settings import JWT_SECRET
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import redirect
from .models import User

#----------Credentials----------
def custom_login(email: str, password: str, type=None):
    try:
        user = User.objects.get(pk=email)
    except User.DoesNotExist:
        return None
    if check_password(password, user.password): return user
    else: return None

def set_credential(response: Response, user: User):
    if user is not None:
        encoded = jwt.encode({"user_email": user.user_email, "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=1)}, JWT_SECRET, algorithm="HS256")
        response.set_cookie('jwt', encoded, domain=".ace.project")
        return response

def register(email: str, password: str, user_name: str):
    isValid = re.search('([a-zA-Z0-9-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(\.[a-zA-Z0-9-]*)*', email)
    if isValid is None: raise ValidationError('Not a valid email format')
    if bool(email and password and user_name):
        salt = salt_generator()
        db_passwd = db_password_generator(password, salt)
        new_user = User.objects.create(user_email=email, password=db_passwd, enable_time=timezone.now(), user_name=user_name)
    else:
        raise Exception

def not_authed(request: HttpRequest):
    if request.session.get("user_email") is None: return True
    return False

def check_password(password: str, db_passwd: str):
    temp = db_passwd.split('$')
    salt = temp[0]
    hashed = temp[1]
    if hashlib.sha256((password+salt).encode('utf8')).hexdigest() == hashed: return True
    return False

def db_password_generator(password: str, salt: str):
    hashed = hashlib.sha256((password + salt).encode('utf8')).hexdigest()
    return f"{salt}${hashed}"

def salt_generator():
     return "".join([uuid.uuid4().hex for x in range(2)])

def get_user(request: HttpRequest):
    user = User.objects.get(pk=request.session.get("user_email"))
    return user

#----------others----------