from django.urls import  path
from .import views


urlpatterns =[
    path('', views.student_index_view, name='student_index'),
    path('register/', views.student_register, name='student_register'),
]