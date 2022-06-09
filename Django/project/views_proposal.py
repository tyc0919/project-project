import datetime
import uuid
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Activity, Job, JobDetail, City, Collaborator, JobStatus
from .modules import *
from django.utils import timezone

##----------Proposal----------

def my_proposal(request):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)

    not_fin_list = []
    for a in Activity.objects.filter(owner=user, is_finished=0):
        a.post_time = a.post_time.strftime("%Y/%m/%d")
        jobs = Job.objects.filter(activity=a)
        for job in jobs:
            job.dead_line = job.dead_line.strftime("%Y/%m/%d")
        
        not_fin_list.append({
            "activity_object": a,
            "jobs": jobs
        })
        
    
    
    
    fin_list = []
    for a in Activity.objects.filter(owner=user, is_finished=1):
        a.post_time = a.post_time.strftime("%Y/%m/%d")
        jobs = Job.objects.filter(activity=a)
        for job in jobs:
            job.dead_line = job.dead_line.strftime("%Y/%m/%d")
        
        fin_list.append({
            "activity_object": a,
            "jobs": jobs
        })
        
        
    # fetch all collab activities
    try:
        all_collab = Collaborator.objects.filter(user_email=user)
    except:
        all_collab = None
        
    for collab in all_collab:
        print(collab.activity.activity_name)
        
    data = {
        "user": user,
        "not_finished": not_fin_list,
        "finished": fin_list,
        "all_collab": all_collab
    }

    return render(request, 'myproposal.html', data)

#------------------------------------------------------------------------------------

def proposal_checked(request, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    
    activity = get_activity(activity_id, user)
    
        
    # activity = get_object_or_404(Activity, pk=activity_id, owner=user)
   
        
    jobs = Job.objects.filter(activity_id=activity)
    job_and_detail = []
    for job in jobs:
        job_detail = JobDetail.objects.filter(job=job)
        job_and_detail.append(
            {
                "job_object": job,
                "job_details": job_detail
            }
        )

    data = {"pairs": job_and_detail, "user": user, 'activity': activity}


    return render(request, 'proposal_checked.html', data)

#------------------------------------------------------------------------------------

def proposal_create(request: HttpRequest):
    # add this line as long as the view requires the user stay logged in
    if request.method == "POST":
        if not_authed(request): return redirect('index')
        try:
            user = get_user(request)
            activity_name = request.POST.get("activity_name")
            data = {'cities': City.objects.all()}
            if activity_name.strip("") == "":
                data["alert"] = '請填寫企劃名稱'
                return render(request, 'proposal_create.html', data)
            elif len(activity_name) > 30: 
                data["alert"] = '企劃名稱過長'
                return render(request, 'proposal_create.html', data)

            city = City.objects.get(pk=request.POST.get("city"))
            invitation_code = uuid.uuid4().hex.upper()[:20]
            a = Activity.objects.create(owner=user, city=city, activity_name=activity_name, is_public=0, is_finished=0, post_time=timezone.now(), invitation_code=invitation_code)
            collaborator = Collaborator.objects.create(activity=a, user_email=user)
        except Exception:
            print(Exception)

        return redirect('myproposal')
    else:
        if not_authed(request): return redirect('index')
        user = get_user(request)
        data = {
            'cities': City.objects.all(),
        }
        return render(request, 'proposal_create.html', data)

#------------------------------------------------------------------------------------

def proposal_create_function1(request: HttpRequest, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    collaborators = Collaborator.objects.filter(activity=a)
    data = {
        'user': user,
        'activity': a,
        'collaborators': collaborators
    }
    if request.method == 'POST':
        data['alert'] = '新增成功'
        try:
            person_in_charge = get_object_or_404(User, pk=request.POST.get("person_in_charge_email"))
            dead_line = datetime.datetime.strptime(request.POST.get("dead_line"), "%Y-%m-%d").date()
            job = Job.objects.create(
                activity=a, 
                person_in_charge_email=person_in_charge, 
                title=request.POST.get("title"), 
                status=JobStatus.objects.get(pk=1), 
                order=3, 
                create_time=timezone.now(), 
                dead_line=dead_line,
                content=request.POST['content'])
            # 記得改order 資料表有問題
        except ObjectDoesNotExist:
            data['alert'] = '該人員不存在'

        return render(request, 'proposal_create_function1.html', data)

    return render(request, 'proposal_create_function1.html', data)

#------------------------------------------------------------------------------------

def proposal_create_function2(request, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    jobs = Job.objects.filter(activity=a)
    job_and_detail = []
    for job in jobs:
        job_detail = JobDetail.objects.filter(job=job)
        job_and_detail.append(
            {
                "job_object": job,
                "job_details": job_detail
            }
        )
    data = {
        'user': user,
        'activity': a,
        'pairs': job_and_detail
    }
    
    return render(request, 'proposal_create_function2.html', data)

#------------------------------------------------------------------------------------

def proposal_create_function2_1(request: HttpRequest,activity_id=None,job_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    job = get_object_or_404(Job, pk=job_id, activity=a)
    job_details = JobDetail.objects.filter(job=job)
    collaborators = Collaborator.objects.filter(activity=a)
    a = job.activity
    data = {
        'user': user,
        'activity': a,
        'job': job,
        'job_details': job_details,
        'collaborators': collaborators,
    }
    if request.method == 'POST':
        data['alert'] = '更新成功'
        try:
            person_in_charge = get_object_or_404(User, pk=request.POST.get("person_in_charge_email"))
            dead_line = datetime.datetime.strptime(request.POST.get("dead_line"), "%Y-%m-%d").date()
            job.dead_line = dead_line
            job.title = request.POST.get("title")
            job.person_in_charge_email = person_in_charge
            job.content = request.POST.get("content")
            job.save()
        except ObjectDoesNotExist:
            data['alert'] = '該人員不存在'
        

        return render(request, 'proposal_create_function2_1.html', data)
    else:
        return render(request, 'proposal_create_function2_1.html', data)

#------------------------------------------------------------------------------------

def proposal_create_function3(request, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    data = {
        'user': user,
        'activity': a,
    }
    # email功能尚未解鎖

    return render(request, 'proposal_create_function3.html', data)

#------------------------------------------------------------------------------------

def proposal_create_function4(request, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    collaborators = Collaborator.objects.filter(activity=a)
    data = {
        'user': user,
        'activity': a,
        'collaborators': collaborators
    }

    return render(request, 'proposal_create_function4.html', data)

#------------------------------------------------------------------------------------

def proposal_post(request, activity_id=None):
    # add this line as long as the view requires the user stay logged in
    if not_authed(request): return redirect('index')
    user = get_user(request)
    a = get_activity(activity_id, user)
    data = {
        'user': user,
        'activity': a,
    }
    if request.method == 'POST':
        data["alert"] = "公開成功"
        a.content = request.POST.get("content")
        a.is_public = 1
        a.save()
        return render(request, 'proposal_post.html', data)
    return render(request, 'proposal_post.html', data)

#------------------------------------------------------------------------------------

def proposal_job_delete(request, activity_id=None, job_id=None):
    user = get_user(request)
    a = get_activity(activity_id, user)
    job = get_object_or_404(Job, pk=job_id, activity=a)
    job.delete()
    return redirect(f'/proposal_checked/{activity_id}')

def proposal_delete(request, activity_id=None):
    user = get_user(request)
    a = get_activity(activity_id, user)
    a.delete()
    return redirect(my_proposal)

def proposal_join(request, invitation_code):
    if request.method == "POST":
        user = get_user(request)
        data = {'status': 'success', 'message': '已成功加入該企劃!'}
        try:
            a = get_object_or_404(Activity, invitation_code=invitation_code)
            collab_user = Collaborator.objects.create(activity=a, user_email=user)
        except:
            data = {'status': 'fail', 'message': '此邀請碼不存在或已經是協作者了!'}
        return JsonResponse(data)
    return JsonResponse({'status': 'fail', 'message': '此邀請碼不存在!'})

def get_activity(activity_id, user):
    try:
        activity = Activity.objects.get(id=activity_id, owner=user)
        return activity
    except:
        pass
    
    try:
        activity = Activity.objects.get(id=activity_id)
        collab = Collaborator.objects.get(activity=activity, user_email=user)
        return activity
    except:
        pass
    
    return get_object_or_404(Activity, pk=activity_id, owner=user)
