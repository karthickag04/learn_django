from django.urls import  path
from .import views


urlpatterns =[
    path('', views.teachers_index_view, name='teachers_index'),
]