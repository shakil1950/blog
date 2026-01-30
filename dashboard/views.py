from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCatgoryForm,PostForm,UserForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User


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
    return render(request,'dashboard/categories.html')


@login_required
def add_categories(request):

    if request.method=='POST':
        forms=AddCatgoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,f'Category {{forms.category}} added successfully')
            forms=AddCatgoryForm()
            return redirect('categories')
    
    forms=AddCatgoryForm()
    context={
        'forms':forms
    }
    return render(request,'dashboard/categories_add.html',context)

@login_required
def edit_categories(request,id):
    category=Category.objects.get(id=id)
    if request.method=='POST':
        form=AddCatgoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully edited')
            form=AddCatgoryForm()
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
    context={
        'post':post
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
            post.slug=slugify(title)
            post.save()
            messages.success(request,'Post successfully created')
            return redirect('view_post')
        else:
            forms=PostForm()
            return redirect('add_post')
    forms=PostForm()

    print(forms)
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
            dataSave.slug=slugify(forms.cleaned_data['title'])
            dataSave.save()
            messages.success(request,'Post edit successfully!')
            return redirect('view_post')
        else:
            messages.error(request,f'Error->{{forms.errors}}')
            print(forms.errors)
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
    context={
        'users':user
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