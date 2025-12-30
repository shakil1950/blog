from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status="Published")
    sample_post=Blog.objects.filter(status="Published",is_featured=False)
    context={
        "categories":categories,
        "featured_post":featured_post,
        "sample_post":sample_post
    }
  
    return render(request,'home/home.html',context)