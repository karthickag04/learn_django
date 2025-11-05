from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser



# method 2 for user registration by extending UserCreationForm
class CustomRegisterForm(UserCreationForm):

    # ROLE_CHOICES = [
    #     ('student', 'Student'),
    #     ('teacher', 'Teacher'),
    # ]


    # role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")

    date_of_birth = forms.DateField(required=False, label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role', 'phone_number', 'address', 'date_of_birth']


