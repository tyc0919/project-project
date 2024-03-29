from django.urls import path
from  .views_api import *


urlpatterns = [
    # path('', , name=""),
    path('csrf-get/', CSRFEndpoint.as_view(), name='csrf-get'),                                        # get csrf token
    path('login/', SignIn.as_view(), name="login"),                                                    # login
    path('signup/', SignUp.as_view(), name="signup"),                                                  # sign up
    path('logout/', Logout.as_view(), name="logout"),                                                  # logout
    path('join-activity/code/',JoinActivityWithCode.as_view(), name="join-code"),                      # Join activities with invitation_code
    path('leave-activity/',LeaveActivity.as_view(), name="leave"),                                     # Join activities with invitation_code

    path('activity/',GetActivityCards.as_view() , name="activity-cards"),                              # get activities info for default page    
    path('activity/<int:activity_id>/',GetActivity.as_view() , name="activity"),                       # get certain activity info
    path('activity/<int:activity_id>/job/', GetJob.as_view() , name="activity-jobs"),                            # get all jobs for certain activity
    path('activity/<int:activity_id>/job/<int:job_id>/', GetCertainJob.as_view() , name="certain-job"),   # get certain job from activity 
    path('activity/create/',CreateActivity.as_view() , name="create-activity"),                        # create a new activity
    path('activity/update/',UpdateActivity.as_view(), name="update-activity"),                         # update an existing activity
    path('activity/delete/',DeleteActivity.as_view() , name="delete-activity"),                        # delete an existing activity
    path('activity/publish/',PublishActivity.as_view() , name="publish-activity"),                     # publish an exising activity
    path('activity/finish/',FinishActivity.as_view() , name="finish-activity"),                        # finish an existing activity
    path('activity/budget/update/',UpdateActivityBudget.as_view() , name="update-activity-budget"),    # update the budget for a certain activity        
    path('activity/<int:activity_id>/collaborator/',GetCollaborator.as_view() , name="get-collaborator"),# get the collaborators of a certain activity                                                                    
    path('activity/<int:activity_id>/budget/',GetBudget.as_view() , name="get-budget-page"),           # get info of budget page

    path('myjob/',GetMyJob.as_view() , name="myjob"),                                                  # get all jobs of the logged in user
    path('job/create/',CreateJob.as_view() , name="create-job"),                                       # create new job
    path('job/update/',UpdateJob.as_view(), name="update-job"),                                        # update a existing job
    path('job/delete/',DeleteJob.as_view(), name="delete-job"),                                        # delete a existing job
    path('job/status/',StatusJob.as_view(), name="status-job"),                                        # change status of a existing job

    path('activity/<int:activity_id>/job/<int:job_id>/job_detail/',GetJobDetail.as_view() , name="get-job-detail"),  # get job details for a certain job
    path('job-detail/create/',CreateJobDetail.as_view() , name="create-job-detail"),                   # create job detail 
    path('job-detail/delete/',DeleteJobDetail.as_view() , name="delete-job-detail"),                   # delete job detail
    path('job-detail/update/',UpdateJobDetail.as_view() , name="update-job-detail"),                   # update job detail content and title
    path('job-detail/status/',StatusJobDetail.as_view() , name="status-job-detail"),                   # update job detail status

    path('userprofile/',GetUserProfile.as_view() , name="userprofile"),                                # get user profile of the logged in user             
    path('userprofile/edit/',UpdateUserProfile.as_view() , name="update-userprofile"),                 # edit the logged in user's profile                
    path('userprofile/resetpassword/',UpdateUserPassword.as_view() , name="reset-password"),           # update the logged in user's password

    path('social/',GetSocial.as_view() , name="get-social"),                                           # get all public activities
    path('social/<int:activity_id>/',GetPublicActivity.as_view() , name="get-public-activity"),        # get a specific published activity
    path('social/<int:activity_id>/review/',GetReview.as_view() , name="get-review"),                  # get reviews of a published activity
    path('social/post-review/',PostReview.as_view() , name="post-review"),                             # post review to a published avticity
    path('social/update-review/',UpdateReview.as_view() , name="update-review"),                       # update user review

    path('file/activity/<int:activity_id>/',GetActivityFile.as_view() , name="get-activity-file"),     # get all files of a specific activity
    path('file/job/<int:job_id>/',GetJobFile.as_view() , name="get-job-file"),                         # get all files of a specific job
    path('upload/job/',UploadJobFile.as_view() , name="upload-job-file"),                              # upload file to specific job                        
    path('upload/avatar/',UploadUserAvatar.as_view() , name="upload-user-avatar"),                     # upload user avatar
    path('upload/expenditure/',UploadExpenditure.as_view() , name="upload-expenditure"),               # upload expenditure to a specific activity
    path('upload/activity_pic/', UploadActivityPic.as_view(), name="upliad-activity-pic"),             # upload picture for a specific activity
    path('delete-file/',DeleteFile.as_view() , name="delete-file"),                                    # delete specific file
    path('serve-file/<int:activity_id>/<str:file_name>',ServeFile.as_view() , name="serve-file"),     # serve file
    path('serve-file/avatar/<str:user_email>',ServeAvatar.as_view() , name="serve-avatar"),         # serve file
    path('serve-file/activity-pic/<str:activity_picture>',ServeActivityPic.as_view() , name="serve-activity-pic"),        # serve file

    path('log/<int:activity_id>/',GetLog.as_view() , name="get-log"),                                  # get all logs for a specific activity

    # path('test/', TestView.as_view(), name="test"),
]   
