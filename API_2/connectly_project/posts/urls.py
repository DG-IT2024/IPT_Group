from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [

    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<int:id>/', views.update_user, name='update_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),

    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    # path('posts/update/<int:id>/', views.update_post, name='update_post'),  # New update route
    # path('posts/delete/<int:id>/', views.delete_post, name='delete_post'),  # New delete route

  ]

