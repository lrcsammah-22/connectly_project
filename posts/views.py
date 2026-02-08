from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsPostAuthor 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

class PostDetailView(APIView): 
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated, IsPostAuthor] 
    
    def get(self, request, pk): 
        if pk == 0:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)  
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post) 
        serializer = PostSerializer(post)
        return Response({"content": serializer.data}) 

    def post(self, request, pk=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """EDIT A POST"""
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """DELETING A POST """
        post = get_object_or_404(Post, pk=pk)
        
        self.check_object_permissions(request, post)
        
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated!"})

class UserListCreate(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreate(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListCreate(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#FOR LOGIN SAMPLE
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
                "message": "Login successful!"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "error": "Invalid credentials"
        }, status=status.HTTP_401_UNAUTHORIZED)