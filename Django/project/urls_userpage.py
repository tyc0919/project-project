from django.urls import path, include
from django.urls import re_path as url
from  . import views_userpage

urlpatterns = [
    path('event_index/', views_userpage.event_index, name="event_index"),
    path('information/', views_userpage.information, name="information"),
]   
