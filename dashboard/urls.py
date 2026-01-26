from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('Category/',views.categories,name='categories'),
    path('Category/edit/<int:id>',views.edit_categories,name='edit_categories'),
    path('Category/delete/<int:id>',views.delete_categories,name='delete_categories'),
    path('Category/add',views.add_categories,name='add_categories'),


]
