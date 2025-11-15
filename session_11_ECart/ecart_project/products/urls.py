from django.urls import path
from . import views

urlpatterns = [
    path('products_list/', views.show_products, name='products_list'),
]