import re
import uuid
import os
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from . import modules
from .models import Activity
from .models import User
from .models import Job
from .modules import *

##----------User Area-----------

def event_index(request):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    answer_dic = {}
    
    data_A = Activity.objects.filter(owner = user)[0:5].values()
    data_A = list(data_A)
    answer_dic['activities'] = data_A

    data_W = Job.objects.filter(person_in_charge_email = user).order_by('-create_time')[0:5].values()
    data_W = list(data_W)
    answer_dic['Jobs'] = data_W

    data_W2 = Job.objects.filter(person_in_charge_email = user).order_by('dead_line')[0:5].values()
    data_W2 = list(data_W2)
    answer_dic['Jobs2'] = data_W2
    
    answer_dic['user'] = user

    return render(request, 'event_index.html' , answer_dic)

def information(request:HttpRequest):
    if not_authed(request): return redirect('index')
    
    user = get_user(request)
    data = {'pic':user.picture_path ,'name' : user.user_name ,'email' : user.user_email}

    if request.POST:
        temp_user = User.objects.get(user_email = user.user_email)
        temp_user.user_name = request.POST.get('name')
        temp_user.save()
        user = get_user(request)
        data = {'pic':user.picture_path ,'name' : user.user_name ,'email' : user.user_email}
        # return render(request, 'information.html', data)

    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        if  myfile: # files判斷檔案
            file_name = uuid.uuid4().hex + ".jpg"
            with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/project/avatar/' + file_name , 'wb+') as destination:
                for chunk in myfile.chunks():
                    destination.write(chunk)
            user.picture_path = file_name
            user.save()
            data['pic'] = user.picture_path
            return render(request, 'information.html', data)
    return render(request, 'information.html', data)

    # return render(request, 'information.html', data)

    