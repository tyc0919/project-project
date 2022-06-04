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

##----------Proposal----------

def my_proposal(request):
    return render(request, 'myproposal.html')

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