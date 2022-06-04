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

##----------Social----------

def social_index(request):
    return render(request, 'social_index.html')

def social_checked(request):
    return render(request, 'social_checked.html')

def social_comment(request):
    return render(request, 'social_comment.html')

def mysocial(request):
    return render(request, 'mysocial.html')