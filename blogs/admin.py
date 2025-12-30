from django.contrib import admin
from .models import Category,Blog
# Register your models here.
admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):
    list_display=['title','author',
                  'short_descriptions',
                  'created_at','is_featured',
                  'status']
    prepopulated_fields={'slug':('title',)}
    search_fields=('id','title','category__category_name','status')
    list_editable=['is_featured']
    list_per_page=10
    
   


admin.site.register(Blog,BlogAdmin)
