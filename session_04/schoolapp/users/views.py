from django.shortcuts import render
from .forms import ManualRegisterForm, CustomRegisterForm, AuthenticationForm

# Create your views here.

def register_view(request):
    # reg_form = ManualRegisterForm()
    reg_form = CustomRegisterForm()
    return render(request, 'users/register.html', {'register_form': reg_form})

def login_view(request):
    if request.method == 'GET':
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    elif request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if username == 'karthickag04' and password == 'Welcome@123p':
            return render(request, 'students/index.html')

        return render(request, 'users/login.html', {'error': 'Invalid credentials'})

def index_view(request):
    return render(request, 'index.html')