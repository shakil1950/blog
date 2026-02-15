from django import forms
from blogs.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddCatgoryForm(forms.ModelForm):

    class Meta:
        model=Category
        fields='__all__'


class PostForm(forms.ModelForm):
    
    class Meta:
        model=Blog
        fields=['title','category','featured_image','short_descriptions','blog_body']
        labels={
            'short_descriptions':'Description',
            'blog_body':'Write Content',
            'is_featured':'Featured This Post'
        }

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_active']

class EditUserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','last_name','is_active']