from django.shortcuts import render,redirect
from blogs.models import Category,Blog,AboutUs,SocialMediaLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    about_us=AboutUs.objects.last()
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status="Published")
    sample_post=Blog.objects.filter(status="Published",is_featured=False)
    context={
        "categories":categories,
        "featured_post":featured_post,
        "sample_post":sample_post,
        "about_us":about_us
    }
  
    return render(request,'home/home.html',context)


def registration(request):

    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form=RegistrationForm()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'authentication/registration.html',context)

def login(request):

    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if  user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                return redirect('login')
    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'authentication/login.html',context)
def logout(request):
    auth.logout(request)
    return redirect('login')

