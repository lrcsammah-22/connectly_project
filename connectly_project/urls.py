from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication (dj-rest-auth + allauth)
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

    # API endpoints
    path('posts/', include('posts.urls')),  # all posts-related routes
    path('users/', include('posts.urls')),  # if you still want /users/ for Homework 5
]