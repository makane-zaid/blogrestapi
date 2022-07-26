from rest_framework import status, mixins, generics, permissions, viewsets
from blog.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from blog.models import Post
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import PostSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from django.db.models import Q

    
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
        
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset= Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Post.objects.all().exclude(private=True)
        elif self.request.user.is_superuser:
            return super().get_queryset(*args, **kwargs)
        return super().get_queryset(*args, **kwargs).exclude(~Q(author=self.request.user), private=True)
        
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user