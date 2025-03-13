from django.db.models import Max, Min, Count, Avg
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from instagram.serializers import PostModelSerializer
from instagram.models import Post


# Create your views here.


# class PostList(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request, format=None):
#         data = {
#             'data' : {
#                 'message': 'Hello World',
#                 'status_code': 404,
#             }
#         }
#         return Response(data)


# @api_view(['GET'])
# def post_list(request):
#     data = {
#         'data': {
#             'message': 'Hello World',
#             'success': True
#         }
#     }
#     return Response(data, status=status.HTTP_200_OK)


# class PostList(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         data = []
#         for post in posts:
#             data.append({
#                 'id':post.id,
#                 'title':post.title,
#                 'created_at':post.created_at
#             })
#         return Response(data)


class PostList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializers = PostModelSerializer(posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class PostDetail(APIView):
    def get(self, request, pk, format=None):
        post = Post.objects.get(id=pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)