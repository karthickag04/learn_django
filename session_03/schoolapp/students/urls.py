from django.urls import  path
from .import views


urlpatterns =[
    path('', views.student_index_view, name='student_index'),
]