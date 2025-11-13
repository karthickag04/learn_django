from django.urls import path
from . import views


app_name = 'ecart'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Cart routes
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_cart_view, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.remove_cart_view, name='remove_cart'),
    # Checkout flow
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-summary/', views.order_summary_view, name='order_summary'),
    # User auth routes
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    # Payment simulation routes
    path('payment/', views.payment_page_view, name='payment_page'),
    path('payment/success/', views.payment_success_view, name='payment_success'),
    path('payment/cancel/', views.payment_cancel_view, name='payment_cancel'),
    path('search/', views.search_products, name='search'),

    

]
