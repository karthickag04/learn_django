from django.shortcuts import render

# Create your views here.

def register_view(request):
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if username == 'karthickag04' and password == 'Welcome@123p':
            return render(request, 'students/index.html')

        return render(request, 'users/login.html', {'error': 'Invalid credentials'})

def index_view(request):
    return render(request, 'index.html')