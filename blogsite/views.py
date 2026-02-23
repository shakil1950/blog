from django.shortcuts import render,redirect
from blogs.models import Category,Blog,AboutUs,SocialMediaLink
from django.contrib import auth
from django.core.paginator import Paginator
def home(request):
    about_us=AboutUs.objects.last()
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status="Published")
    sample_post=Blog.objects.filter(status="Published",is_featured=False)
    paginator = Paginator(sample_post, 4)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    context={
        "categories":categories,
        "featured_post":featured_post,
        "sample_post":posts,
        "about_us":about_us
    }
  
    return render(request,'home/home.html',context)


