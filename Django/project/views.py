from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


#----------Not Required Login----------

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def social(request):
    return render(request, 'social.html')

def forgetpasswd(request):
    return render(request, 'forgetpasswd.html')

def logout(request):
    return render(request, 'index.html')

#----------Required Login----------

def event_index(request):
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