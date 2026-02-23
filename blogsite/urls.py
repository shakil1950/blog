
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf import settings
from blogs.sitemaps import PostSitemap
from blogs import views as blog_views
from django.http import HttpResponse

sitemaps = {
 'posts': PostSitemap,
}
def robots_txt(request):
    lines = [
        "User-agent: *",           
        "Disallow: /admin/",       
        "Disallow: /accounts/",    
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('category/',include('blogs.urls')),
    path('<slug:slug>',blog_views.blog_detail,name='blog_detail'),
    path('blogs/search/',blog_views.search,name='search'),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/',include('accounts.urls')),
    path('sitemap.xml',sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt),
    path('social/accounts/', include('allauth.urls')),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
