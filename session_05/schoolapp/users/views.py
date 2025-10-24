from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import ManualRegisterForm, CustomRegisterForm, AuthenticationForm

# Create your views here.

# def register_view(request):
#     # reg_form = ManualRegisterForm()
#     reg_form = CustomRegisterForm()
#     return render(request, 'users/register.html', {'register_form': reg_form})

def register_view(request):
    if request.method == 'POST':
        reg_form = CustomRegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save(commit=False)
            user.email = reg_form.cleaned_data['email']
            user.save()  # saves to auth_user

            # Assign user to the chosen group
            role = reg_form.cleaned_data['role']
            group = Group.objects.get(name=role + 's')  # expects groups "students" or "teachers"
            user.groups.add(group)

            messages.success(request, f"Account created successfully for {user.username} as a {role}.")
            return redirect('login')  # redirect to login page after registration
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
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