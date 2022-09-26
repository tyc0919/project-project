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
    path('activity/<int:activity_id>/budget/',GetBudget.as_view() , name="get-budget-page"),           # get info of budget page
    path('myjob/',GetMyJob.as_view() , name="myjob"),                                                  # get all jobs of the logged in user
    path('activity/<int:activity_id>/job/<int:job_serial_number>/job_detail/',GetJobDetail.as_view() , name="get-job-detail"),  # get job details for a certain job
    path('job-detail/create/',CreateJobDetail.as_view() , name="create-job-detail"),                   # create job detail 
    path('job-detail/delete/',DeleteJobDetail.as_view() , name="delete-job-detail"),                   # delete job detail
    path('job-detail/update/',UpdateJobDetail.as_view() , name="update-job-detail"),                   # update job detail content and title
    path('job-detail/status/',StatusJobDetail.as_view() , name="status-job-detail"),                   # update job detail status
    path('userprofile/',GetUserProfile.as_view() , name="userprofile"),                                # get user profile of the logged in user             
    path('userprofile/edit/',UpdateUserProfile.as_view() , name="update-userprofile"),                 # edit the logged in user's profile                
    path('userprofile/resetpassword/',UpdateUserPassword.as_view() , name="reset-password"),           # update the logged in user's password
    path('social/',GetSocial.as_view() , name="get-social"),                                           # get all public activities
    path('social/<int:activity_id>/',GetPublicActivity.as_view() , name="get-public-activity"),        # get certain published activity
    path('upload/job/',UploadJobFile.as_view() , name="upload-job-file"),                              # upload file to specific job                        
    path('upload/avatar/',UploadUserAvatar.as_view() , name="upload-user-avatar"),                     # upload user avatar
    path('upload/expenditure/',UploadExpenditure.as_view() , name="upload-expenditure"),               # upload expenditure to specific activity
    path('upload/activity_pic/', UploadActivityPic.as_view(), name="upliad-activity-pic"),             # upload picture for specific activity
    path('test/', TestView.as_view(), name="test"),
]   
