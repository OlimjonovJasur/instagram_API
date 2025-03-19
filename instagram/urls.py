from django.urls import path
from instagram import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/delete/', views.PostTwoDeleteView.as_view(), name='post-delete'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
]