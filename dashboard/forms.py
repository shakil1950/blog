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
        fields=['title','category','featured_image','short_descriptions','blog_body','status','is_featured']
        labels={
            'short_descriptions':'Description',
            'blog_body':'Write Content',
            'is_featured':'Featured This Post'
        }

class UserForm(UserCreationForm):
    class meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']