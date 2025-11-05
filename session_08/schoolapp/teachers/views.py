from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Lecture
from .forms import LectureForm

# Create your views here.


def teachers_index_view(request):
    return render(request, 'teachers/index.html')


@login_required
def upload_media(request):
    if request.user.role != 'teacher':
        messages.error(request, 'Only teachers can upload lectures.')
        return redirect('teachers:index')
    
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.teacher = request.user
            lecture.save()
            messages.success(request, 'Lecture uploaded successfully!')
            return redirect('teachers:media_list')
    else:
        form = LectureForm()
    
    return render(request, 'teachers/upload_media.html', {'form': form})


@login_required
def media_list(request):
    if request.user.role == 'teacher':
        lectures = Lecture.objects.filter(teacher=request.user)
    else:
        lectures = Lecture.objects.all()
    
    paginator = Paginator(lectures, 10)  # Show 10 lectures per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'teachers/media_list.html', {'page_obj': page_obj})
