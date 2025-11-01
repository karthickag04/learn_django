from django.shortcuts import render

# Create your views here.


def teacher_index_view(request):
    return render(request, 'teachers/teachers_index.html')


def teacher_profile_view(request):
    return render(request, 'teachers/teachers_profile.html')


def teacher_details_view(request):
    return render(request, 'teachers/teachers_details.html')
