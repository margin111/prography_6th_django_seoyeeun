from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Posts
from django.views import View
from django.views import generic


from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# Create your views here.
