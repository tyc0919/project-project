import re
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from . import modules
from .modules import not_authed
# Create your views here.

#---------Test-----------

# def test(request: HttpRequest):
#     if request.method == "GET": return render(request, 'signin.html')
#     if request.POST:
#         request.session["test"] = "test"
#         return redirect(test)

#----------Not Required Login----------

def index(request):
    return render(request, 'index.html')

def signin(request: HttpRequest):
    if request.POST:
        user = modules.custom_login(request.POST.get("user_email"), request.POST.get("password"))
        print(user)
        if user is not None:
            request = modules.set_credential(request, user)
            return redirect(index)
        else:
            data = {'status': 'fail', 'message':'帳號或密碼有誤'}
            return render(request, 'signin.html', data)
    else: return render(request, 'signin.html')

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

        return render(request, 'signup.html', data)
    return render(request, 'signup.html', data)

def social(request):
    return render(request, 'social.html')

def forgetpasswd(request):
    return render(request, 'forgetpasswd.html')

def logout(request: HttpRequest):
    request.session.flush()
    return redirect(index)

#----------Required Login----------

def event_index(request):
    if not_authed(request): return redirect(index) # add this line as long as the view requires the user stay logged in

    return render(request, 'event_index.html')

##----------User Area-----------

def information(request):
    return render(request, 'information.html')

##----------Proposal----------

def my_proposal(request):
    return render(request, 'my_proposal.html')

def proposal_checked(request):
    return render(request, 'proposal_checked.html')

def proposal_create(request):
    return render(request, 'proposal_create.html')

def proposal_create_function1(request):
    return render(request, 'proposal_create_function1.html')

def proposal_create_function2(request):
    return render(request, 'proposal_create_function2.html')

def proposal_create_function2_1(request):
    return render(request, 'proposal_create_function2_1.html')

def proposal_create_function3(request):
    return render(request, 'proposal_create_function3.html')

def proposal_create_function4(request):
    return render(request, 'proposal_create_function4.html')

def proposal_post(request):
    return render(request, 'proposal_post.html')

##----------Work----------

def mywork(request):
    return render(request, 'mywork.html')

def work_checked_proposal(request):
    return render(request, 'work_checked_proposal.html')

def work_checked(request):
    return render(request, 'work_checked.html')

def work_checked2(request):
    return render(request, 'work_checked2.html')

def work_checked3(request):
    return render(request, 'work_checked3.html')

def work_checked4(request):
    return render(request, 'work_checked4.html')

##----------Collab----------

def colla_index(request):
    return render(request, 'colla_index.html')

def colla_checked(request):
    return render(request, 'colla_checked.html')

##----------Social----------

def my_community(request):
    return render(request, 'my_community.html')

def blog_details(request):
    return render(request, 'blog_details.html')

#----------custom functions-----------