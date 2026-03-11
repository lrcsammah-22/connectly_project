from django.urls import path
from .views import (
    UserListCreate,
    PostListCreate,
    CommentListCreate,
    ProtectedView,
    LoginView,
    PostDetailView,
    LikePostView,
    CommentPostView
)

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/create/', UserListCreate.as_view(), name='user-create'),

    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/comment/', CommentPostView.as_view(), name='post-comment'),

    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]