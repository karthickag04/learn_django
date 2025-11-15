from django.shortcuts import render
from .models import ProductAll

# Create your views here.

def show_products(request):

    productall_list= ProductAll.objects.filter(is_active=True)
    # for product in productall_list:
    #     print(product.product_name, product.image)
    print(productall_list.count())
    return render(request, 'products/index.html', {'productlist': productall_list})