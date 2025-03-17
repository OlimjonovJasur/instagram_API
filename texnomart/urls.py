from django.urls import path
from texnomart import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('images/', views.ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', views.ImageRetrieveUpdateDestroyView.as_view(), name='image-detail'),
]
