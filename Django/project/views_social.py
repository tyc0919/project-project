from logging import exception
import re
from tkinter import EXCEPTION
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from . import modules
from .models import Activity
from .models import User
from .models import Job
from .models import Review
from .modules import *

##----------Social----------

def social_index(request):

    if not_authed(request): 
        return redirect('index')
    
    user = get_user(request)

    temp = Activity.objects.all().filter(is_public = 1)
    data = {'articles' : temp}
    data['user'] = user

    return render(request, 'social_index.html', data)

def social_checked(request, activity_Id):
    
    if not_authed(request): 
        return redirect('index')

    data ={}
    user = get_user(request)

    temp = Activity.objects.get(id = activity_Id)
    data['post'] = temp

    temp2 = Review.objects.filter(activity_id = activity_Id)
    temp2 = list(temp2)
        
    data['reviews'] = temp2

    data['activity_id'] = activity_Id

    data['user'] = user

    return render(request, 'social_checked.html', data)

def social_comment(request:HttpRequest, activity_Id):

    user = get_user(request)
    temp = Activity.objects.get(id = activity_Id)
    temp2 = User.objects.get(user_email = user.user_email)
    data ={}

    
    if request.POST:
        star = request.POST.get("rating")
        if star is not None:
            star = int(star)
            
            try:
                id = Review.objects.all().latest('id').id + 1
            except:
                id = 1
                
            if star > 0 and star <= 5:
                Review.objects.create(
                    id = id,
                    activity = temp,
                    reviewer= temp2,
                    content = request.POST.get("review_comment"),
                    review_time = timezone.now(),
                    review_star = int(request.POST.get("rating"))
                )
        return redirect('social_checked',activity_Id)
    
    return render(request, 'social_comment.html')

def mysocial(request):

    if not_authed(request): 
        return redirect('index')

    user = get_user(request)
    data = {}

    temp = Activity.objects.filter(owner = user.user_email).filter(is_public = 1).values()
    temp = list(temp)

    for x in temp:
        x['review_count'] = Review.objects.filter(activity_id = x['id']).count()

    for y in temp:
        count = 0
        sum = 0
        temp2 = list(Review.objects.filter(activity_id = x['id']).values())
        for z in temp2:
            sum = sum + z['review_star']
            count = count + 1
        y['review_score'] = sum / count

    data = {'datas': temp}
    data['user'] = user

    return render(request, 'mysocial.html', data)