from django.urls import include,path
from django.urls import re_path as url
from testApp import views
from django.contrib import admin

from django.http.response import HttpResponse
from django.http.request import HttpRequest

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    # 首頁
    url(r'^$',views.index,name='index'),  
    url(r'^signup/',views.signUp,name='signup'), 
    url(r'^signin/',views.signIn,name='signin'),
    
    
    # /test--------
    # activity
    # url(r'^activity', views.activityApi),
    # url(r'^activity/([0-9]+)$',views.activityApi),
]   

urlpatterns += staticfiles_urlpatterns()