from django.contrib import admin
from .models import Category,Blog,SocialMediaLink,AboutUs,Comments
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','author',
                  'short_descriptions',
                  'created_at','is_featured',
                  'status']
    prepopulated_fields={'slug':('title',)}
    search_fields=('id','title','category__category_name','status')
    list_editable=['is_featured','status']
    list_per_page=10
    
    
   

admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(SocialMediaLink)
admin.site.register(AboutUs)
admin.site.register(Blog,BlogAdmin)
