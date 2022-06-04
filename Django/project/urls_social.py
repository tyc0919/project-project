from django.urls import path, include
from django.urls import re_path as url
from  . import views_social

urlpatterns = [
    path('social_index/', views_social.social_index, name="social_index"),
    path('social_checked/', views_social.social_checked, name="social_checked"),
    path('social_comment/', views_social.social_comment, name="social_comment"),
    path('mysocial/', views_social.mysocial, name="mysocial"),
]   
