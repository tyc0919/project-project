from django.urls import path, include
from django.urls import re_path as url
from  .views import test

urlpatterns = [
    path('test/', test, name="test")
]
