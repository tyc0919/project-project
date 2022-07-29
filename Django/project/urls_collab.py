from django.urls import path, include
from django.urls import re_path as url
from  . import views_collab

urlpatterns = [
    path('colla_index/', views_collab.colla_index, name="colla_index"),
    path('colla_checked/<str:shop_email>', views_collab.colla_checked, name="colla_checked"),
]   
