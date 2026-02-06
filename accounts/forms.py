from django.contrib.auth import get_user_model
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['email','username','password1','password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields='__all__'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avater','dob','bio']