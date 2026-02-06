from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.contrib.auth.models import User
# Register your models here.


class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False
    verbose_name_plural='profile'

class AdminUser(UserAdmin):
    inlines=[ProfileInline]


admin.site.unregister(User)
admin.site.register(User,AdminUser)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     fields=['user','avater','bio','dob']
