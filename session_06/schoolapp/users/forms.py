from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User


# method 1 for user registration using built-in UserCreationForm
# class ManualRegisterForm(forms.Form):
#     username = forms.CharField(max_length=150, required=True)
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput, required=True)
#     password2 = forms.CharField(widget=forms.PasswordInput, required=True)


# method 2 for user registration by extending UserCreationForm
class CustomRegisterForm(UserCreationForm):

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


