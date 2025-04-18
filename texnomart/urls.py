from django.db import router
from django.urls import path
from texnomart import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'products-url', views.ProductViewSet)

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('images/', views.ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', views.ImageRetrieveUpdateDestroyView.as_view(), name='image-detail'),
    path('comment/', views.CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentListByProductView.as_view(), name='comment_list_by_product')
]

# urlpatterns += router.urls