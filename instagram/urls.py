from django.urls import path
from instagram import views
from instagram import customobtainview

urlpatterns = [
    path('post-list/', views.PostListView.as_view(), name='post-list'),
    path('post-list/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-list/<int:pk>/delete/', views.PostTwoDeleteView.as_view(), name='post-delete'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('custom-token/', customobtainview.CustomAuthToken.as_view(), name='custom-token'),
    path('logout/', customobtainview.LogoutApiView.as_view(), name='logout'),
]