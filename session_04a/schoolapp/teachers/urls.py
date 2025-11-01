
from django.urls import path
from . import views


urlpatterns = [
 path('', views.teacher_index_view, name='teacher_index'),
 path('teacher_profile/', views.teacher_profile_view, name='teacher_profile'),
 path('teacher_details/', views.teacher_details_view, name='teacher_details'),
]