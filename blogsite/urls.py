
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('category/',include('blogs.urls')),
    path('<slug:slug>/',blog_views.blog_detail,name='blog_detail'),
    path('blogs/search/',blog_views.search,name='search'),
    path('user/register/',views.registration,name='registration'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
