from django.db import models

# Create your models here.

# from django.db import models

class StudentProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=5, blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_no})"


class AssignmentSubmission(models.Model):
    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    lecture = models.ForeignKey('teachers.Lecture', on_delete=models.CASCADE)
    video_answer = models.FileField(upload_to='assignments/video/', blank=True, null=True)
    audio_answer = models.FileField(upload_to='assignments/audio/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        unique_together = ['student', 'lecture']  # One submission per student per lecture

    def __str__(self):
        return f"{self.student.username} - {self.lecture.title}"
