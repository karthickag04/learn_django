from django import forms
from .models import Lecture, Feedback
from students.models import StudentProfile

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'video', 'audio']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter lecture title',
                'maxlength': '200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Enter detailed lecture description'
            }),
            'video': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'video/*'
            }),
            'audio': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'audio/*'
            }),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 20:
            raise forms.ValidationError("Description must be at least 20 characters long.")
        return description
    
    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        audio = cleaned_data.get('audio')
        
        if not video and not audio:
            raise forms.ValidationError("Please upload at least one media file (video or audio).")
        
        # Check file sizes
        if video and video.size > 100 * 1024 * 1024:  # 100MB
            raise forms.ValidationError("Video file size must be less than 100MB.")
        
        if audio and audio.size > 50 * 1024 * 1024:  # 50MB
            raise forms.ValidationError("Audio file size must be less than 50MB.")
        
        return cleaned_data


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'feedback_text']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control'
            }),
            'feedback_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your feedback for the student...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show students in the dropdown
        self.fields['student'].queryset = StudentProfile.objects.all().order_by('first_name', 'last_name')
        self.fields['student'].empty_label = "Select a student"
    
    def clean_feedback_text(self):
        feedback_text = self.cleaned_data.get('feedback_text')
        if len(feedback_text) < 10:
            raise forms.ValidationError("Feedback must be at least 10 characters long.")
        return feedback_text