from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from texnomart.models import Product, Comment

from rest_framework import generics
from texnomart.models import Category, Product, Image, Comment
from texnomart.serializers import CategorySerializer, ProductModelSerializer, ImageModelSerializer, CommentModelSerializer



# Category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




# Product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


#Image
class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer


class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer


#Comment
class CommentListView(ListAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()


class CommentListByProductView(ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self, *args, **kwargs):
        product_id = self.kwargs['pk']
        queryset = Comment.objects.filter(product_id=product_id)
        return queryset



















# class CategoryList(APIView):
#     ...
#
#
# class ProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductModelSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
