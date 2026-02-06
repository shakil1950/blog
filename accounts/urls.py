from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/post',views.profile_wise_post,name='profile-wise-post'),
    path('profile/edit',views.edit_profile,name='edit-profile'),
    path('profile/change-password',views.change_password,name='change-password'),
    path('profile/reset-password',views.reset_password,name='reset-password'),
]
