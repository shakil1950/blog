from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/post',views.profile_wise_post,name='profile-wise-post'),
    path('profile/post/edit/<slug:slug>',views.edit_post_profile_wise,name='edit_post_profile_wise'),
    path('profile/post/delete/<slug:slug>',views.delete_post_profile_wise,name='delete_post_profile_wise'),
    path('profile/edit/<int:id>/',views.edit_profile,name='edit-profile'),
    path('profile/change-password',views.change_password,name='change-password'),
    path('profile/reset-password',views.reset_password,name='reset-password'),
]
