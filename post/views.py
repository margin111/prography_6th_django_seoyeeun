from rest_framework.generics import ListAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import PostSerializer ,PostDetailSerializer ,PostCreateSerializer
from .models import Posts
from django.views import View
from django.views import generic


from django.shortcuts import render



class PostViewSet(ListAPIView):
    queryset = Posts.objects.order_by('-postid')

    serializer_class = PostSerializer


class PostViewSet_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer


class PostViewSet_update(UpdateAPIView):
    lookup_field = 'no'
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostViewSet_delete(DestroyAPIView):
    lookup_field = 'no'
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostViewSet_create(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer




# Create your views here.
