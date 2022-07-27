from rest_framework import serializers

from product.models import Comment,ProductImage,Product



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('rate','content')
        
        
class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image','is_main')
        
class ProductImageCommentListSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True)
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        
