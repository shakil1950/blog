from django.contrib.sitemaps import Sitemap
from .models import Blog

class PostSitemap(Sitemap):
 changefreq = 'weekly'
 priority = 0.9
  
 def get_urls(self, site=None, **kwargs):
        # এখানে site=None দিলে জ্যাঙ্গো ডাটাবেসের example.com ইগনোর করবে
        return super(PostSitemap, self).get_urls(site=None, **kwargs)
 def items(self):
    return Blog.objects.all()

 def lastmod(self, obj):
    return obj.updated_at
