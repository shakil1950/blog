from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views
from .views import CustomResetPasswordView
urlpatterns = [
    path('register/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('password_reset/', CustomResetPasswordView.as_view(), name='password-reset'),
    
    # ২. ইমেইল পাঠানো হয়েছে এমন কনফার্মেশন পেজ
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    
    # ৩. ইমেইলের লিঙ্কে ক্লিক করলে যে পেজ আসবে (টোকেন ভেরিফিকেশন)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    
    # ৪. পাসওয়ার্ড সফলভাবে রিসেট হওয়ার পেজ
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/',views.profile,name='profile'),
    path('profile/post',views.profile_wise_post,name='profile-wise-post'),
    path('profile/post/edit/<slug:slug>',views.edit_post_profile_wise,name='edit_post_profile_wise'),
    path('profile/post/delete/<slug:slug>',views.delete_post_profile_wise,name='delete_post_profile_wise'),
    path('profile/edit/<int:id>/',views.edit_profile,name='edit-profile'),
    path('profile/change-password',views.change_password,name='change-password'),
    path('activate/<uid64>/<token>/', views.activate_user, name='activate_user'),
    
  
]
