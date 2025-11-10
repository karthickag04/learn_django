from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CustomRegisterForm, AuthenticationForm
from django.contrib.auth import authenticate, login

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

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if you have only student module
            # return render(request, 'students/index.html') # you can use redirect as well given below
            # return redirect('students_index')  # replace with your named URL

            # if you have both student and teacher modules and admin panel
            if user.groups.filter(name='teachers').exists():
                # return render(request, 'teachers/index.html')  # or: return redirect('teachers_index')
                return redirect('teachers:index')  # or: return redirect('teachers_index')
            elif user.groups.filter(name='students').exists():
                return redirect('students:index')  # or: return redirect('students_index')
            # elif user.groups.filter(name='admin').exists():
            #     return render(request, 'adminpanel/index.html')  # or: return redirect('adminpanel_index')
            else:
                messages.error(request, "No role assigned to your account.")
                return redirect('login')

        return render(request, 'users/login.html', {'error': 'Invalid credentials'})

def index_view(request):
    return render(request, 'users/index.html')