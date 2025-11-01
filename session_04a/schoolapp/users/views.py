from django.shortcuts import render
from .other_python_forms import *


# Create your views here.

def starting_index(request):
    return render(request, 'index.html')







def register(request):

    myform = my_registeration_form()

    return render(request, 'users/register.html', {'use_this_form':myform})

def login(request):
    return render(request, 'users/login.html')
