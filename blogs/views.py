from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comments
from django.db.models import Q
from django.contrib.auth.decorators import login_required



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
    same_blog=Blog.objects.filter(category=blog.category).exclude(id=blog.id)
   
    if request.method=='POST':
        com=Comments()
        com.user=request.user
        com.blog=blog
        com.comment=request.POST['comment']
        com.save()
        return HttpResponseRedirect(request.path)
    comment=Comments.objects.filter(blog=blog,status='show')
    com_paginator=Paginator(comment,3)
    page_number = request.GET.get('page', 1)
    comments = com_paginator.get_page(page_number)
    all_comment_blog=comment.count()
    context={
        'blog':blog,
        'comments':comments,
        'all_comment_blog':all_comment_blog,
        'same_blog':same_blog
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