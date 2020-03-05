from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('postid','title','content','date')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        field = ('postid','title','content','date')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title','content','date')
