from django.urls import  path
from .import views

app_name = 'teachers'

urlpatterns =[
    path('', views.teachers_index_view, name='index'),
    path('upload/', views.upload_media, name='upload_media'),
    path('media/', views.media_list, name='media_list'),
]