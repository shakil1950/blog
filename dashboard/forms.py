from django import forms
from blogs.models import Category,Blog

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