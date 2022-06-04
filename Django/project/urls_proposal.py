from django.urls import path, include
from django.urls import re_path as url
from  . import views_proposal

urlpatterns = [
    path('myproposal/', views_proposal.my_proposal, name="myproposal"),
    path('proposal_checked/', views_proposal.proposal_checked, name="proposal_checked"),
    path('proposal_create/', views_proposal.proposal_create, name="proposal_create"),
    path('proposal_create_function1/', views_proposal.proposal_create_function1, name="proposal_create_function1"),
    path('proposal_create_function2/', views_proposal.proposal_create_function2, name="proposal_create_function2"),
    path('proposal_create_function2_1/', views_proposal.proposal_create_function2_1, name="proposal_create_function2_1"),
    path('proposal_create_function3/', views_proposal.proposal_create_function3, name="proposal_create_function3"),
    path('proposal_create_function4/', views_proposal.proposal_create_function4, name="proposal_create_function4"),
    path('proposal_post/', views_proposal.proposal_post, name="proposal_post"),
]   
