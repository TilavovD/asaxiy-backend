from django.shortcuts import render
from .serializer import CommentSerializer, ProductSerializer, CategorySerializer
from .models import Product, Category, Comment
from rest_framework import generics
from helpers.pagination import CustomPagination
from django.views.decorators.vary import vary_on_headers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductCommentList(generics.ListAPIView):

    # Create a new attribute to store the serializers
    serializer_class = ProductSerializer
    queryset = Product.objects.all().prefetch_related("comments", "saveds", "images")
    pagination_class=CustomPagination
    # permission_classes = [IsAuthenticated]
    filterset_fields = ['category']
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class CategoryProductCommentList(generics.RetrieveAPIView):
    
    # Create a new attribute to store the serializers
    serializer_class = CategorySerializer
    queryset = Category.objects.all().last()
    pagination_class=CustomPagination
    
    # filterset_fields = ['category']

    def get_queryset(self, *args, **kwargs):
        print(kwargs)   
        # category_id = self.kwargs['id']


class UserComments(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    

    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)      

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
    