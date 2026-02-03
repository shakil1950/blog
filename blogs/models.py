from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

STATUS_CHOICES=[
    ("Draft","Draft"),
    ("Published","Published")
]  
COMMENTS_CHOICES_STATUS=[
    ('show','show'),
    ('hide','hide')
]  
class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%y/%m/%d')
    short_descriptions=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default="Draft")
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class AboutUs(models.Model):
    content=models.TextField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"About Us - {self.created_at.strftime('%Y-%m-%d')}"

class SocialMediaLink(models.Model):
    platform_name=models.CharField(max_length=100,blank=False)
    url=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField(blank=False,null=False)
    status=models.CharField(choices=COMMENTS_CHOICES_STATUS,default='show',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    