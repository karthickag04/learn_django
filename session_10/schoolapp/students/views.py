from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .form import StudentRegistrationForm, AssignmentForm
from .models import AssignmentSubmission
from teachers.models import Lecture

# Create your views here.

def student_index_view(request):
    return render(request, 'students/index.html')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_register')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/student_form.html', {'form': form})


@login_required
def upload_assignment(request, lecture_id=None):
    if request.user.role != 'student':
        messages.error(request, 'Only students can submit assignments.')
        return redirect('students:index')
    
    lecture = None
    if lecture_id:
        lecture = get_object_or_404(Lecture, id=lecture_id)
    
    # Check if student already submitted for this lecture
    if lecture:
        existing_submission = AssignmentSubmission.objects.filter(
            student=request.user, lecture=lecture
        ).first()
        if existing_submission:
            messages.warning(request, 'You have already submitted an assignment for this lecture.')
            return redirect('students:assignment_list')
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = request.user
            assignment.save()
            messages.success(request, 'Assignment submitted successfully!')
            return redirect('students:assignment_list')
    else:
        form = AssignmentForm()
        if lecture:
            form.initial['lecture'] = lecture
    
    return render(request, 'students/assignment_upload.html', {
        'form': form, 
        'lecture': lecture
    })


@login_required
def assignment_list(request):
    if request.user.role == 'student':
        assignments = AssignmentSubmission.objects.filter(student=request.user)
    else:
        assignments = AssignmentSubmission.objects.all()
    
    # Also get available lectures for students to submit assignments
    available_lectures = Lecture.objects.all().order_by('-uploaded_at')
    if request.user.role == 'student':
        # Filter out lectures where student already submitted
        submitted_lecture_ids = assignments.values_list('lecture_id', flat=True)
        available_lectures = available_lectures.exclude(id__in=submitted_lecture_ids)
    
    paginator = Paginator(assignments, 10)  # Show 10 assignments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/assignment_list.html', {
        'page_obj': page_obj,
        'available_lectures': available_lectures
    })