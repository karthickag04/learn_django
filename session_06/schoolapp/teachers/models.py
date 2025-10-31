from django.db import models

# Create your models here.
# from django.db import models
from students.models import StudentProfile
from django.contrib.auth.models import User

class Feedback(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student} - {self.teacher.username}"
