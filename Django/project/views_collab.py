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

##----------Collab----------

def colla_index(request):
    return render(request, 'colla_index.html')

def colla_checked(request):
    return render(request, 'colla_checked.html')
