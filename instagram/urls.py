from django.contrib import admin
from django.urls import path, include
from instagram import views
from instagram.views import PostList

urlpatterns = [
    path('post-list/', views.PostList.as_view(), name='post-list'),
    path('post-detail/', views.PostDetail.as_view(), name='post-detail'),
]