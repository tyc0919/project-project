import re
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from . import modules
from .models import Activity
from .models import User
from .models import Job
from .modules import *


# Create your views here.

#---------Test-----------

# def test(request: HttpRequest):
#     if request.method == "GET": return render(request, 'signin.html')
#     if request.POST:
#         request.session["test"] = "test"
#         return redirect(test)

#----------Not Required Login----------

def index(request: HttpRequest):
    data = {'response': request.session.get('user_email')}
    return render(request, 'index.html', data)

def signin(request: HttpRequest):
    data={}
    if request.POST:
        user = modules.custom_login(request.POST.get("user_email"), request.POST.get("password"))
        print(user)
        if user is not None:
            request = modules.set_credential(request, user)
            return redirect('event_index')
        else:
            data = {'status': 'fail', 'message':'帳號或密碼有誤'}
    return render(request, 'signin.html', data)

def signup(request: HttpRequest):
    data = {}
    if request.POST:
        try:
            modules.register(request.POST.get("user_email"), request.POST.get("password"), request.POST.get("user_name"))
            data = {'response': '註冊成功!'}
        except ValidationError:
            data = {'response': 'Email格式輸入錯誤'}
        except IntegrityError:
            data = {'response': '該Email已經被註冊'}
        except Exception:
            data = {'response': '欄位不能為空'}

        return redirect('signin')
    return render(request, 'signup.html', data)

def forgetpasswd(request):
    return render(request, 'forgetpasswd.html')

def logout(request: HttpRequest):
    request.session.flush()
    return redirect(index)

#----------Required Login----------

#----------custom functions-----------