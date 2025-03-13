from django.urls import path
from texnomart import views

urlpatterns = [
    path('products/', views.ProductAPIView.as_view(), name='product-list'),
]
