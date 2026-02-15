
from accounts.models import Profile
from .models import Category

def category_processors(request):
    categories=Category.objects.all()
    return dict(categories=categories)


def profile_processors(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.prof_user
            return {'profile': profile} # ডিকশনারি রিটার্ন করা হয়েছে
        except:
            return {'user_profile': None}
            
    return {} # ইউজার লগইন না থাকলেও একটি খালি ডিকশনারি রিটার্ন করতে হবে