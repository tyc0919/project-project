from django.urls import path
from  .views_api import *


urlpatterns = [
    path('csrf-get/', CSRFEndpoint.as_view(), name='csrf-get'),
    path('login/', SignIn.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('test/', TestView.as_view(), name="test"),
]   
