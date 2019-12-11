from django.views import generic
from .models import Blog

from django.shortcuts import render, get_object_or_404
# creating API
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
# def index(request):
#     blogs = Blog.get_all_blogs()

#     return render(request, 'index.html',{'blogs':blogs})
class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Blog.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
# class BlogDetail(generic.DetailView):
#     model = Blog
#     template_name = 'blog_detail.html'


   