from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCatgoryForm



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
    return redirect('categories')