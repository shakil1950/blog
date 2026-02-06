from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from blogs.models import Blog
from dashboard.forms import PostForm
# Create your views here.


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
                if request.user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('home')
            else:
                return redirect('login')
    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'authentication/login.html',context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def profile(request):
    # info=Profile.objects.get(user=request.user)
    context={
        
    }

    return render(request,'authentication/profile.html',context)

@login_required
def profile_wise_post(request):
    posts=Blog.objects.filter(status='Published',author=request.user)
    number_of_post=posts.count()
    # latest=posts.latest('created')
    draft=Blog.objects.filter(status='Draft',author=request.user).count()
    form=PostForm()
    context={
        'posts':posts,
        
        'number_post':number_of_post,
        'draft':draft,
        'form':form
    }
    return render(request,'authentication/profile-wise-post.html',context)

@login_required
def edit_profile(request):
    return render(request,'authentication/edit-profile.html')
@login_required
def change_password(request):
    return render(request,'authentication/change-password.html')
@login_required
def reset_password(request):
    return render(request,'authentication/reset-password.html')