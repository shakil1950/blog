from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('category/',views.categories,name='categories'),
    path('category/edit/<int:id>',views.edit_categories,name='edit_categories'),
    path('category/delete/<int:id>',views.delete_categories,name='delete_categories'),
    path('category/add',views.add_categories,name='add_categories'),
    path('post/',views.view_post,name='view_post'),
    path('post/add',views.add_post,name='add_post'),
    path('post/edit/<slug>',views.edit_post,name='edit_post'),
    path('post/delete/<slug>',views.delete_post,name='delete_post'),
    path('user/',views.view_user,name='view_user'),
    path('user/add',views.add_user,name='add_user'),

]
