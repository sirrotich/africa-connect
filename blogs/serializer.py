from rest_framework import serializers
from .models import Blog

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'author','updated_on','content','created_on','status','category','blog_image')
