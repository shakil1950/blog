from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Category
from django.db.models import Q



def post_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    # try:
    #     category=Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')
    category=get_object_or_404(Category,id=category_id)
    context={
        "posts":posts,
        'category':category
    }

    return render(request,'home/post_by_category.html',context)

def blog_detail(request,slug):
    blog=get_object_or_404(Blog,slug=slug,status='Published')
 
    context={
        'blog':blog
    }
    return render(request,'home/blog_detail.html',context)

def search(request):
    keyword=request.GET.get('keywords')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) |Q (short_descriptions__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'kewword':keyword
    }
    return render(request,'home/search.html',context)