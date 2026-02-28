import uuid
from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCatgoryForm,PostForm,UserForm,EditUserForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render (request,'dashboard/dashboard.html',context)

@login_required
def categories(request):
  
    form=AddCatgoryForm()
    
    context={
        'form':form,
        
    }
    return render(request,'dashboard/categories.html',context)


@login_required
def add_categories(request):

    if request.method=='POST':
        forms=AddCatgoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,f'Category added successfully')
            forms=AddCatgoryForm()
            return redirect('categories')
    
    forms=AddCatgoryForm()
   
    return redirect('categories')

@login_required
def edit_categories(request,id):
    category=get_object_or_404(Category,id=id)
    if request.method=='POST':
        form=AddCatgoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully edited')
            form=AddCatgoryForm()
            return redirect('categories')
        else:
            messages.error(request,'Name already taken')
            return redirect('categories')
    form=AddCatgoryForm(instance=category)
    context={
        'form':form
    }
    return render(request,'dashboard/categories_edit.html',context)

@login_required
def delete_categories(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    messages.success(request,'Successfully Deleted')
    return redirect('categories')

@login_required
def view_post(request):
    post=Blog.objects.all()
    post_paginator=Paginator(post,4)
    page_number = request.GET.get('page', 1)
    posts = post_paginator.get_page(page_number)
    context={
        'post':posts
    }
    return render(request,'dashboard/post.html',context)
@login_required
def add_post(request):

    if request.method=='POST':
        forms=PostForm(request.POST,request.FILES)
        if forms.is_valid():
            post=forms.save(commit=False)
            post.author=request.user
            title=forms.cleaned_data['title']
            base_slug=slugify(title)
            post.slug=f"{base_slug}-{str(uuid.uuid4())[:4]}"
            post.save()
            messages.success(request,'Post successfully created')
            return redirect('view_post')
        else:
            forms=PostForm()
            return redirect('add_post')
    forms=PostForm()

  
    context={
        'forms':forms
    }
    return render(request,'dashboard/add_post.html',context)


@login_required
def edit_post(request,slug):
    post=get_object_or_404(Blog,slug=slug)

    if request.method=='POST':
        forms=PostForm(request.POST,instance=post)
        if forms.is_valid():
            dataSave=forms.save(commit=False)
            base_slug=slugify(forms.cleaned_data['title'])
            dataSave.slug=f"{base_slug}-{str(uuid.uuid4())[:4]}"
            dataSave.status='Draft'
            dataSave.save()
            messages.success(request,'Post edit successfully!')
            return redirect('view_post')
        else:
            messages.error(request,f'Error->{{forms.errors}}')
            
            return redirect('edit_post')
    forms=PostForm(instance=post)
    context={
        'forms':forms
    }
    return render(request,'dashboard/edit_post.html',context)

@login_required
def delete_post(request,slug):
    post=get_object_or_404(Blog,slug=slug)
    post.delete()
    messages.success(request,'Post deleted')
    return redirect('view_post')

@login_required
def view_user(request):
    user=User.objects.all().exclude(id=request.user.id)
    user_paginator=Paginator(user,4)
    page_number = request.GET.get('page', 1)
    users=user_paginator.get_page(page_number)
    context={
        'users':users
    }
    return render(request,'dashboard/user.html',context)

@login_required
def add_user(request):

    if request.method=='POST':
        forms=UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,'user created successfully')
            return redirect('view_user')
        else:
            forms=UserForm()

    forms=UserForm()

    context={
        'forms':forms
    }

    return render(request,'dashboard/add_user.html',context)

@login_required
def edit_user(request,id):
    user=get_object_or_404(User,id=id)
    forms=EditUserForm(instance=user)
    context={
        'forms':forms
    }
    return render(request,'dashboard/edit_user.html',context)

@login_required
def delete_user(request,id):
    user=get_object_or_404(User,id=id)
    user.delete()
    return redirect('view_user')