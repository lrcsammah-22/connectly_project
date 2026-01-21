from django.urls import path
from . import views

urlpatterns = [
    # User routes
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # Post routes
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/update/<int:post_id>/', views.update_post, name='update_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]