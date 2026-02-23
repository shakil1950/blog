from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

User=get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already used")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avater','dob','bio','profession']

        widgets={
            'avater':forms.FileInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'profession':forms.TextInput(attrs={'class':'form-control'})
        }

class ChangePaswordForm(forms.Form):
    prev_pass=forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={
            'class':'form-control passfield',
            'placeholder':'Enter current password'
        })
    )
    pass1=forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control passfield',
                'placeholder':'Enter new password'
            }
        )
    )
    pass2=forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class':'form-control passfield',
            'placeholder':'Enter confirm password'
        })
    )

    def clean(self):
        cleaned_data=super().clean()
        pass1=cleaned_data.get('pass1')
        pass2=cleaned_data.get('pass2')

        if pass1 and pass2 and pass1!=pass2:
            raise forms.ValidationError('Password not match')
        return cleaned_data
