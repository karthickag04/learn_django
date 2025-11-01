from django.shortcuts import render

# Create your views here.
from .forms import StudentProfileForm

def student_index_view(request):
    return render(request, 'students/student_index.html')

def student_profile_view(request):

    student_profile_form = StudentProfileForm()
    
    return render(request, 'students/student_profile.html', {'use_student_profile_form':student_profile_form})

def student_details_view(request):
    return render(request, 'students/student_details.html')

