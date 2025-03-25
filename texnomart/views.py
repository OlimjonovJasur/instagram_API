from functools import cached_property

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from texnomart.models import Product, Comment

from rest_framework import generics
from texnomart.models import Category, Product, Image, Comment
from texnomart.serializers import CategorySerializer, ProductModelSerializer, ImageModelSerializer, CommentModelSerializer


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductModelSerializer
    # pagination_class = (LimitOffsetPagination,)

    def get_queryset(self):
        cache_key = 'product-list'
        cached_products = cache.get(cache_key)
        if not cached_products:
            cached_products = Product.objects.all().select_related('category').prefetch_related('likes').prefetch_related('images')
            cache.set(cache_key, cached_products, timeout=60 * 2)
            print('Cache o\'rnatildi')

        return cached_products

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListCreateView, self).dispatch(request, *args, **kwargs)


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



# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductModelSerializer
#     queryset = Product.objects.all()

















# class CategoryList(APIView):
#     ...
#
#
# class ProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductModelSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
