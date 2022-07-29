import re
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from . import modules
from .models import Activity
from .models import User
from .models import Job
from .models import Shop
from .modules import *

##----------Collab----------

def colla_index(request):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    shops = Shop.objects.all()
    
    data= {}
    data['user'] = user
    data['shops'] = shops
    
    return render(request, 'colla_index.html', data)

def colla_checked(request, shop_email):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the shop doesn't exist
    try:
        shop = Shop.objects.get(pk=shop_email)
    except Exception:
        return redirect('index')
    
    data= {}
    data['user'] = user
    data['shop'] = shop
    
    return render(request, 'colla_checked.html', data)
