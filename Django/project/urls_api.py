from django.urls import path
from  .views_api import *


urlpatterns = [
    # path('', , name=""),
    path('csrf-get/', CSRFEndpoint.as_view(), name='csrf-get'),
    path('login/', SignIn.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('activity/',GetActivityCards.as_view() , name="activity-cards"),
    path('activity/<int:activity_id>/',GetActivity.as_view() , name="activity"),
    path('myjob/',GetMyJob.as_view() , name="myjob"),
    path('test/', TestView.as_view(), name="test"),
]   
