from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from testApp.models import User
from testApp.Serializers import *
# Create your views here.

# views
    
def index(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request,'signup.html')

def signIn(request):
    return render(request, 'signin.html')



# api
class RegisterAPI(generics.GenericAPIViews):
    serializer = self.get_serializer







# /------ api-test
@csrf_exempt
def userApi(request,id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer= UserSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method =='POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        user_data=JSONParser().parse(request)
        user = User.objects.get(Account=user_data['Account'])
        users_serializer = UserSerializer(user,data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        user = User.objects.get(Account=id)
        user.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
    
@csrf_exempt
def activityApi(request,id=0):
    if request.method == 'GET':
        activitys = Activity.objects.all()
        activitys_serializer= ActivitySerializer(activitys,many=True)
        return JsonResponse(activitys_serializer.data,safe=False)
    elif request.method =='POST':
        activity_data = JSONParser().parse(request)
        activitys_serializer = ActivitySerializer(data=activity_data)
        if activitys_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        activity_data=JSONParser().parse(request)
        activity = Activity.objects.get(Id=activity_data['id'])
        activitys_serializer = ActivitySerializer(activity,data=activity_data)
        if activitys_serializer.is_valid():
            activitys_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        activity = Activity.objects.get(Id=id)
        activity.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
@csrf_exempt
def cityApi(request,id=0):
    if request.method == 'GET':
        citys = City.objects.all()
        citys_serializer= CitySerializer(citys,many=True)
        return JsonResponse(citys_serializer.data,safe=False)
    elif request.method =='POST':
        city_data = JSONParser().parse(request)
        citys_serializer = CitySerializer(data=city_data)
        if citys_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        city_data=JSONParser().parse(request)
        city = City.objects.get(Id=city_data['id'])
        citys_serializer = CitySerializer(city,data=city_data)
        if citys_serializer.is_valid():
            citys_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        city = City.objects.get(Id=id)
        city.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
    
@csrf_exempt
def colabShopApi(request,id=0):
    if request.method == 'GET':
        colabShops = ColabShop.objects.all()
        colabShops_serializer= ColabShopSerializer(colabShops,many=True)
        return JsonResponse(colabShops_serializer.data,safe=False)
    elif request.method =='POST':
        colabShop_data = JSONParser().parse(request)
        colabShops_serializer = ColabShopSerializer(data=colabShop_data)
        if colabShops_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        colabShop_data=JSONParser().parse(request)
        colabShop = ColabShop.objects.get(Id=colabShop_data['id'])
        colabShops_serializer = ColabShopSerializer(colabShop,data=colabShop_data)
        if colabShops_serializer.is_valid():
            colabShops_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        colabShop = ColabShop.objects.get(Id=id)
        colabShop.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
@csrf_exempt
def collaboratorApi(request,id=0):
    if request.method == 'GET':
        collaborators = Collaborator.objects.all()
        collaborators_serializer= CollaboratorSerializer(collaborators,many=True)
        return JsonResponse(collaborators_serializer.data,safe=False)
    elif request.method =='POST':
        collaborator_data = JSONParser().parse(request)
        collaborators_serializer = CollaboratorSerializer(data=collaborator_data)
        if collaborators_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        collaborator_data=JSONParser().parse(request)
        collaborator = Collaborator.objects.get(Id=collaborator_data['id'])
        collaborators_serializer = CollaboratorSerializer(collaborator,data=collaborator_data)
        if collaborators_serializer.is_valid():
            collaborators_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        collaborator = Collaborator.objects.get(Id=id)
        collaborator.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
@csrf_exempt
def jobApi(request,id=0):
    if request.method == 'GET':
        jobs = Job.objects.all()
        jobs_serializer= JobSerializer(jobs,many=True)
        return JsonResponse(jobs_serializer.data,safe=False)
    elif request.method =='POST':
        job_data = JSONParser().parse(request)
        jobs_serializer = JobSerializer(data=job_data)
        if jobs_serializer.is_valid():
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method =='PUT':
        job_data=JSONParser().parse(request)
        job = Job.objects.get(Id=job_data['id'])
        jobs_serializer = JobSerializer(job,data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        job = Job.objects.get(Id=id)
        job.delete()
        return JsonResponse('Delete Successfully',safe=False)
# /------api-test


