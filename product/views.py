from django.shortcuts import render
from rest_framework import generics
from helpers.pagination import CustomPagination

from product.models import Product
from product.serializers import ProductImageCommentListSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('comments','images').all()
    serializer_class = ProductImageCommentListSerializer
    pagination_class =CustomPagination
    extensions_auto_optimize = True