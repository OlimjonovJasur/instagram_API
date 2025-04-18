from multiprocessing.managers import Token

from django.core.serializers import serialize
from django.db.models import Max, Min, Count, Avg
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from instagram.serializers import PostModelSerializer, CommentModelSerializer
from instagram.models import Post, Comment
from instagram.permessions import GetOrPostPermission, IsOwner, IsNotAliUpdateDelete, NotDeleteAfterTwoMinutes,  IsWeekday
from rest_framework_simplejwt.authentication import JWTAuthentication


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



# class PostListOrCreate(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializers = PostModelSerializer(posts, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#
#
#     def post(self, request):
#         serializer = PostModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetail(APIView):
#     def get(self, request, pk, format=None):
#         try:
#             post = Post.objects.get(id=pk)
#             serializer = PostModelSerializer(post)
#             return Response(serializer.data)
#         except Post.DoesNotExist:
#             return Response({'error': 'Post does not exists'}, status=status.HTTP_404_NOT_FOUND)
#
#
#     def delete(self, request, pk=None):
#         try:
#             post = Post.objects.get(id=pk)
#             if post:
#                 post.delete()
#                 data = {'message':'Post successfully deleted'}
#                 return Response(data, status=status.HTTP_204_NO_CONTENT)
#         except Post.DoesNotExist:
#             data = {'message': 'post not found'}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)
#
#
#     def put(self, request, pk=None):
#         post = Post.objects.get(pk=pk)
#         serializer = PostModelSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def patch(self, request):
#         ...


class PostListView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    permission_classes = [IsNotAliUpdateDelete]


class PostTwoDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    permission_classes = [NotDeleteAfterTwoMinutes]


class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = [IsWeekday]