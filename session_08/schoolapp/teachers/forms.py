from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'video', 'audio']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lecture title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter lecture description'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'accept': 'video/*'}),
            'audio': forms.FileInput(attrs={'class': 'form-control', 'accept': 'audio/*'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        audio = cleaned_data.get('audio')
        
        if not video and not audio:
            raise forms.ValidationError("Please upload at least one media file (video or audio).")
        
        return cleaned_data