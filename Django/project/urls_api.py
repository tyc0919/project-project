from django.urls import path
from  .views_api import *


urlpatterns = [
    # path('', , name=""),
    path('csrf-get/', CSRFEndpoint.as_view(), name='csrf-get'),                                        # get csrf token
    path('login/', SignIn.as_view(), name="login"),                                                    # login
    path('signup/', SignUp.as_view(), name="signup"),                                                  # sign up      
    path('activity/',GetActivityCards.as_view() , name="activity-cards"),                              # get activities info for default page    
    path('activity/<int:activity_id>/',GetActivity.as_view() , name="activity"),                       # get certain activity info
    path('activity/<int:activity_id>/job/', GetJob.as_view() , name="job"),                            # get all jobs for certain activity
    path('activity/create/',CreateActivity.as_view() , name="create-activity"),                        # create a new activity
    path('activity/update/',UpdateActivity.as_view(), name="update-activity"),                         # update an existing activity
    path('activity/delete/',DeleteActivity.as_view() , name="delete-activity"),                        # delete an existing activity
    path('activity/publish/',PublishActivity.as_view() , name="publish-activity"),                     # publish an exising activity
    path('activity/finish/',FinishActivity.as_view() , name="finish-activity"),                        # finish an existing activity
    path('activity/budget/update/',UpdateActivityBudget.as_view() , name="update-activity-budget"),    # update the budget for a certain activity        
    path('activity/<int:activity_id>/collaborator/',GetCollaborator.as_view() , name="get-collaborator"),# get the collaborators of a certain activity                                                                    
    path('myjob/',GetMyJob.as_view() , name="myjob"),                                                  # get all jobs of the logged in user
    path('activity/<int:activity_id>/job/<int:job_serial_number>/job_detail/',GetJobDetail.as_view() , name="get-job-detail"),  # get job details for a certain job
    path('job-detail/create/',CreateJobDetail.as_view() , name="create-job-detail"),                   # create job detail 
    path('userprofile/',GetUserProfile.as_view() , name="userprofile"),                                # get user profile of the logged in user             
    path('userprofile/edit/',UpdateUserProfile.as_view() , name="update-userprofile"),                 # edit the logged in user's profile                
    path('userprofile/resetpassword/',UpdateUserPassword.as_view() , name="reset-password"),           # update the logged in user's password
    path('social/',GetSocial.as_view() , name="get-social"),                                           # get all public activities
    path('social/<int:activity_id>/',GetPublicActivity.as_view() , name="get-public-activity"),        # get certain published activity

    path('test/', TestView.as_view(), name="test"),
]   
