from django.urls import path, include
from django.urls import re_path as url
from  . import views, views_collab, views_proposal, views_social, views_userpage, views_work

urlpatterns = [
    #path('test/', views.test, name="test"),
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('forgetpasswd/', views.forgetpasswd, name="forgetpasswd"),
    path('logout/', views.logout, name="logout"),
    # #---------------------------------------------
    # path('event_index/', views_userpage.event_index, name="event_index"),
    # path('information/', views_userpage.information, name="information"),
    # #---------------------------------------------
    # path('myproposal/', views_proposal.my_proposal, name="myproposal"),
    # path('proposal_checked/', views_proposal.proposal_checked, name="proposal_checked"),
    # path('proposal_create/', views_proposal.proposal_create, name="proposal_create"),
    # path('proposal_create_function1/', views_proposal.proposal_create_function1, name="proposal_create_function1"),
    # path('proposal_create_function2/', views_proposal.proposal_create_function2, name="proposal_create_function2"),
    # path('proposal_create_function2_1/', views_proposal.proposal_create_function2_1, name="proposal_create_function2_1"),
    # path('proposal_create_function3/', views_proposal.proposal_create_function3, name="proposal_create_function3"),
    # path('proposal_create_function4/', views_proposal.proposal_create_function4, name="proposal_create_function4"),
    # path('proposal_post/', views_proposal.proposal_post, name="proposal_post"),
    # #---------------------------------------------
    # path('mywork/', views_work.mywork, name="mywork"),
    # path('work_checked_proposal/', views_work.work_checked_proposal, name="work_checked_proposal"),
    # path('work_checked/', views_work.work_checked, name="work_checked"),
    # path('work_checked2/', views_work.work_checked2, name="work_checked2"),
    # path('work_checked3/', views_work.work_checked3, name="work_checked3"),
    # path('work_checked4/', views_work.work_checked4, name="work_checked4"),
    # #---------------------------------------------
    # path('colla_index/', views_collab.colla_index, name="colla_index"),
    # path('colla_checked/', views_collab.colla_checked, name="colla_checked"),
    # #---------------------------------------------
    # path('social_index/', views_social.social_index, name="social_index"),
    # path('social_checked/', views_social.social_checked, name="social_checked"),
    # path('social_comment/', views_social.social_comment, name="social_comment"),
    # path('mysocial/', views_social.mysocial, name="mysocial"),
]   
