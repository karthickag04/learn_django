from django import forms
from .models import StudentProfile, AssignmentSubmission
from teachers.models import Lecture

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'roll_no', 'class_name', 'section', 'date_of_birth', 'email', 'phone', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['lecture', 'video_answer', 'audio_answer']
        widgets = {
            'lecture': forms.Select(attrs={'class': 'form-control'}),
            'video_answer': forms.FileInput(attrs={'class': 'form-control', 'accept': 'video/*'}),
            'audio_answer': forms.FileInput(attrs={'class': 'form-control', 'accept': 'audio/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show lectures that exist
        self.fields['lecture'].queryset = Lecture.objects.all().order_by('-uploaded_at')
        self.fields['lecture'].empty_label = "Select a lecture"
    
    def clean(self):
        cleaned_data = super().clean()
        video_answer = cleaned_data.get('video_answer')
        audio_answer = cleaned_data.get('audio_answer')
        
        if not video_answer and not audio_answer:
            raise forms.ValidationError("Please upload at least one answer file (video or audio).")
        
        return cleaned_data
