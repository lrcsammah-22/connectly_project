from django.urls import path
from .views import PostDetailView, LoginView, UserListCreate, PostListCreate, CommentListCreate

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('login/', LoginView.as_view(), name='post-list-create'),
    #path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail-view'),
    path('posts/', PostDetailView.as_view(), name='post-list'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
]