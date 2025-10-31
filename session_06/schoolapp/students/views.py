from django.shortcuts import render, redirect
from .form import StudentRegistrationForm

# Create your views here.

def student_index_view(request):
    return render(request, 'students/index.html')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_register')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/student_form.html', {'form': form})