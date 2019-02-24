from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .models import Post
from .serializers import PostSerializer



# list view

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# create view

class PostCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# read view

class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# update view

class PostUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# delete view

class PostDelete(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
