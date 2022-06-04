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