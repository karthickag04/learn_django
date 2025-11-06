from django.urls import  path
from .import views

app_name = 'teachers'

urlpatterns =[
    path('', views.teachers_index_view, name='index'),
    path('upload/', views.upload_media, name='upload_media'),
    path('media/', views.media_list, name='media_list'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/give/', views.give_feedback, name='give_feedback'),
    path('feedback/give/<int:student_id>/', views.give_feedback, name='give_feedback'),
    path('submissions/', views.view_submissions, name='submissions'),
]