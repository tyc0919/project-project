from django.urls import path
from  .views_api import *


urlpatterns = [
    # path('', , name=""),
    path('csrf-get/', CSRFEndpoint.as_view(), name='csrf-get'),
    path('login/', SignIn.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('activity/',GetActivityCards.as_view() , name="activity-cards"),
    path('activity/<int:activity_id>/',GetActivity.as_view() , name="activity"),
    path('activity/<int:activity_id>/job/', GetJob.as_view() , name="job"),
    path('myjob/',GetMyJob.as_view() , name="myjob"),
    path('userprofile/',GetUserProfile.as_view() , name="userprofile"),
    path('userprofile/edit/',UpdateUserProfile.as_view() , name="update-userprofile"),

    path('test/', TestView.as_view(), name="test"),
]   
