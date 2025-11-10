from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from django.utils import timezone

from users.models import CustomUser
from .models import Attendance, Lecture, Feedback
from .forms import LectureForm, FeedbackForm
from students.models import AssignmentSubmission, StudentProfile

# Create your views here.


def teachers_index_view(request):
    context = {}
    if request.user.is_authenticated and request.user.role == 'teacher':
        # Get teacher's statistics
        lectures_count = Lecture.objects.filter(teacher=request.user).count()
        submissions_count = AssignmentSubmission.objects.filter(lecture__teacher=request.user).count()
        pending_reviews = AssignmentSubmission.objects.filter(lecture__teacher=request.user).count()  # All submissions for now
        
        context.update({
            'lectures_count': lectures_count,
            'submissions_count': submissions_count,
            'pending_reviews': pending_reviews,
        })
    
    return render(request, 'teachers/index.html', context)


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
            messages.success(request, f'Lecture "{lecture.title}" uploaded successfully!')
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
    
    lectures = lectures.order_by('-uploaded_at')
    
    paginator = Paginator(lectures, 12)  # Show 12 lectures per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'teachers/media_list.html', {'page_obj': page_obj})


@login_required
def give_feedback(request, student_id=None):
    if request.user.role != 'teacher':
        messages.error(request, 'Only teachers can give feedback.')
        return redirect('teachers:index')
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.teacher = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('teachers:feedback_list')
    else:
        form = FeedbackForm()
        if student_id:
            try:
                from students.models import StudentProfile

                student = StudentProfile.objects.get(id=student_id)
                form.initial['student'] = student
            except StudentProfile.DoesNotExist:
                messages.error(request, 'Student not found.')
                return redirect('teachers:feedback_list')
    
    return render(request, 'teachers/give_feedback.html', {'form': form})


@login_required
def feedback_list(request):
    if request.user.role == 'teacher':
        feedbacks = Feedback.objects.filter(teacher=request.user)
    else:
        feedbacks = Feedback.objects.all()
    
    feedbacks = feedbacks.order_by('-created_at')
    
    paginator = Paginator(feedbacks, 10)  # Show 10 feedbacks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'teachers/feedback_list.html', {'page_obj': page_obj})


@login_required
def view_submissions(request):
    """View all student submissions for teacher's lectures"""
    if request.user.role != 'teacher':
        messages.error(request, 'Only teachers can view submissions.')
        return redirect('teachers:index')
    
    submissions = AssignmentSubmission.objects.filter(lecture__teacher=request.user)
    submissions = submissions.order_by('-submitted_at')
    
    paginator = Paginator(submissions, 10)  # Show 10 submissions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'teachers/submissions_list.html', {'page_obj': page_obj})


@login_required
def attendance_entry(request):
    if request.user.role != 'teacher':
        messages.error(request, 'Only teachers can manage attendance.')
        return redirect('teachers:index')
    
    if request.method == 'POST':
        # Process attendance submission
        student_ids = request.POST.getlist('student_id')
        for student_id in student_ids:
            attendance_status = request.POST.get(student_id)
            if attendance_status in ['present', 'absent']:
                try:
                    student = StudentProfile.objects.get(id=student_id)
                    # Create or update attendance record
                    attendance, created = Attendance.objects.get_or_create(
                        student=student,
                        teacher=request.user,
                        date=timezone.now().date(),
                        defaults={'status': attendance_status}
                    )
                    if not created:
                        attendance.status = attendance_status
                        attendance.save()
                except StudentProfile.DoesNotExist:
                    continue
        
        messages.success(request, 'Attendance recorded successfully!')
        return redirect('teachers:attendance_entry')




    studentlist = StudentProfile.objects.all()
   
    return render(request, 'teachers/Attendance_entry.html', {'studentlist': studentlist})




@login_required
def attendance_report(request):

    attendance = Attendance.objects.all()
    studentlist = StudentProfile.objects.all()
    return render(request, 'teachers/Attendance_report.html', {'studentlist': studentlist, 'attendance': attendance})

