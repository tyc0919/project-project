import re
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from pymysql import NULL
from . import modules
from .models import Activity, JobDetail
from .models import User
from .models import Job
from .models import JobStatus
from .models import Collaborator
from .modules import *

##----------Work----------



def mywork(request):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    data = {}
    
    # user
    user = get_user(request)
    data['user'] = user
    
    # job
    jobs = Job.objects.filter(person_in_charge_email = user)[:].values()
    data['jobs'] = jobs
    
    for job in jobs:
        # date 
        formatDate = job['dead_line'].strftime("%Y/%m/%d")
        job['dead_line'] = formatDate
        
        # activity
        job['activity']= (Activity.objects.get(pk=job['activity_id']))
        
        # status
        job['status'] = (JobStatus.objects.get(pk=job['status_id']))
    
    return render(request, 'mywork.html', data)


def proposal_work_checked(request: HttpRequest, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
     
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    data['job'] = job
    data['user'] = user
    
    if user == job.person_in_charge_email:
        data['can_be_edited'] = True
    else:
        data['can_be_edited'] = False
        
    return render(request, 'proposal_work_checked.html', data)


def work_checked(request, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    
    # job
    job = Job.objects.get(pk=job_id)
    data['job'] = job

    # user
    data['user'] = user
    
    return render(request, 'work_checked.html', data)

def work_checked2(request: HttpRequest, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    data['user'] = user
    data['job'] = job
    
    if request.POST:
        job_detail_id = JobDetail.objects.all().latest('id').id
        try:
            biggest_order = JobDetail.objects.filter(job=job).latest('order').order
        except:
            biggest_order = 0
            
        new_job_detail = JobDetail.objects.create(
            id=job_detail_id+1,
            job=job, 
            content=request.POST['content_data'], 
            order=biggest_order+1
        )
        
        return redirect('work_checked3', job_id=job_id)
    
    return render(request, 'work_checked2.html', data)

def work_checked3(request, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    data['user'] = user
    data['job'] = job
    
    all_job_detail = JobDetail.objects.filter(job=job).order_by('order')
    data['all_job_detail']= all_job_detail
    
    return render(request, 'work_checked3.html', data)

def work_checked4(request: HttpRequest, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    
    data['user'] = user
    data['job'] = job
    
    if request.POST:
        status = request.POST['status']
        status_id = int(status)
        Job.objects.filter(pk=job.id).update(
            status=JobStatus.objects.get(pk=status_id)
        )
        return redirect('work_checked3',job_id=job_id)
    
    return render(request, 'work_checked4.html', data)

def work_content_update(request: HttpRequest, job_id):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job doesn't exist
    try:
        job = Job.objects.get(pk=job_id)
    except Exception:
        return redirect('index')
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    data['job'] = job
    data['user'] = user
    
    
    if request.POST:
        content = request.POST['content_data']
        Job.objects.filter(id=job_id).update(**{'content': content})
        return redirect('work_checked3', job_id=job.id)

    return render(request, 'work_content_update.html', data)

def work_detail_remove(request: HttpRequest, job_detail_id, counter):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job_detail doesn't exist
    try:
        job_detail = JobDetail.objects.get(pk=job_detail_id)
    except Exception:
        return redirect('index')
    
    # job
    job = job_detail.job
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')

    data = {}
    data['user'] = user
    data['job'] = job
    data['job_detail'] = job_detail
    data['counter'] = counter
    
    if request.POST:
        job_detail.delete()
        return redirect('work_checked3', job.id)
    
    return render(request, 'work_detail_remove.html', data)

def work_detail_update(request: HttpRequest, job_detail_id, counter):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    # if the job_detail doesn't exist
    try:
        job_detail = JobDetail.objects.get(pk=job_detail_id)
    except Exception:
        return redirect('index')
    
    # job
    job = job_detail.job
    
    # if user not in the activity
    if not_in_activity(user, job): return redirect('index')
    
    data = {}
    data['user'] = user
    data['job'] = job
    data['job_detail'] = job_detail
    data['counter'] = counter 
    
    if request.POST:
        content = request.POST['content_data']
        JobDetail.objects.filter(id=job_detail_id).update(**{'content': content})
        return redirect('work_checked3', job_id=job.id)
    
    return render(request, 'work_detail_update.html', data)



# --------------- 判斷 -----------------------------

def not_in_activity(user, job):
    activity = job.activity
    
    try:
        collaborators = Collaborator.objects.filter(activity=activity).values('user_email')
    except:
        collaborators = None
        
    if collaborators == None:
        is_collaborator = False
    elif (user in collaborators):
        is_collaborator = True
    else:
        is_collaborator = False
        
    if not(user == activity.owner) and not(is_collaborator):
        return True
    
    return False
