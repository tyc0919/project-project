from django.urls import path, include
from django.urls import re_path as url
from  . import views_work

urlpatterns = [
    path('mywork/', views_work.mywork, name="mywork"),
    path('proposal_work_checked/<int:job_id>', views_work.proposal_work_checked, name="proposal_work_checked"),
    path('work_checked/<int:job_id>', views_work.work_checked, name="work_checked"),
    path('work_checked2/<int:job_id>', views_work.work_checked2, name="work_checked2"),
    path('work_checked3/<int:job_id>', views_work.work_checked3, name="work_checked3"),
    path('work_checked4/<int:job_id>', views_work.work_checked4, name="work_checked4"),
    path('work_detail_remove/<int:job_detail_id>/<int:counter>', views_work.work_detail_remove, name="work_detail_remove"),
    path('work_detail_update/<int:job_detail_id>/<int:counter>', views_work.work_detail_update, name="work_detail_update"),
    path('work_content_update/<int:job_id>', views_work.work_content_update, name="work_content_update"),
]   
