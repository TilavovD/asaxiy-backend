from rest_framework import serializers
from .models import Category, Product, Comment, ProductImage

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content","product",)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = "__all__"
        lookup_field='slug'

