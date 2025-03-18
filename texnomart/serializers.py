from django.template.context_processors import request
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from texnomart.models import Product, Image, Category, Comment


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many=True, read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)
    likes = serializers.SerializerMethodField()
    slug = serializers.SlugField(source='category.slug', read_only=True)
    avg_rating = serializers.SerializerMethodField()


    def get_likes(self, instance):
        user = self.context.get('request').user
        if not user.is_authenticated:
            return False
        if user not in instance.likes.all():
            return False

        return True

    def get_avg_rating(self, instance):
        ratings = instance.comment_product.values_list('rating', flat=True)
        if ratings:
            avg = sum(ratings) / len(ratings)
            return round(avg)
        return 0

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
