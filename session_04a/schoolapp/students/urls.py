
from django.urls import path
from . import views


urlpatterns = [
 path('', views.student_index_view, name='student_dashboard'),
 path('student_profile/', views.student_profile_view, name='student_profile'),
 path('student_details/', views.student_details_view, name='student_details'),
 
]