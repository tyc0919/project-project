from django.urls import path, include
from django.urls import re_path as url
from  . import views_work

urlpatterns = [
    path('mywork/', views_work.mywork, name="mywork"),
    path('work_checked_proposal/', views_work.work_checked_proposal, name="work_checked_proposal"),
    path('work_checked/', views_work.work_checked, name="work_checked"),
    path('work_checked2/', views_work.work_checked2, name="work_checked2"),
    path('work_checked3/', views_work.work_checked3, name="work_checked3"),
    path('work_checked4/', views_work.work_checked4, name="work_checked4"),
]   
