from django.urls import  path
from .import views

app_name = 'students'

urlpatterns =[
    path('', views.student_index_view, name='index'),
    path('register/', views.student_register, name='student_register'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/upload/', views.upload_assignment, name='upload_assignment'),
    path('assignments/upload/<int:lecture_id>/', views.upload_assignment, name='upload_assignment'),
]