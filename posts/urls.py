from django.urls import path
from .views import FeedView
from .views import (
    UserListCreate,
    PostListCreate,
    PostDetailView,
    LikePostView,
    CommentPostView,
    LoginView,
    ProtectedView,
    FeedView,
)

urlpatterns = [
  # Users
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/create/', UserListCreate.as_view(), name='user-create'),

    # Posts
    path('', PostListCreate.as_view(), name='post-list-create'),  # /posts/
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/comment/', CommentPostView.as_view(), name='post-comment'),

    # Feed (✅ FIXED)
    path('feed/', FeedView.as_view(), name='feed'),

    # Auth / Protected
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]