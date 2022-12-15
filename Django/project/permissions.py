from rest_framework.permissions import BasePermission
from .models import *
from rest_framework.request import Request

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User): return obj == request.user
        if isinstance(obj, Activity): return obj.owner == request.user
        if isinstance(obj, Job): return obj.activity.owner == request.user
        if isinstance(obj, Review): return obj.reviewer == request.user
        # if isinstance(obj, JobDetail): 
        #     j = Job.objects.get(activity_id=obj.activity_id, serial_number=obj.job_serial_number_id)
        #     if j.person_in_charge_email == request.user: return True
        #     return obj.activity.owner == request.user

class IsCollaborator(BasePermission): # Trying to make this obj only accept Activity
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Activity): return True if Collaborator.objects.filter(activity=obj, user_email=request.user) or obj.is_public == 1 else False


class IsResponsible(BasePermission): # probably only needs job for this permission
    def has_object_permission(self, request, view, obj):
        return obj.person_in_charge_email == request.user or obj.activity.owner == request.user
