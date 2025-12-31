

from .models import Category

def category_processors(request):
    categories=Category.objects.all()
    return dict(categories=categories)