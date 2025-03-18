from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=129, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    discount = models.SmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    likes = models.ManyToManyField(User, blank=True)


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    image_text  = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product')
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='comments', null=True, blank=True)
    bad_comment = models.TextField(null=True, blank=True)
    good_comment = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices)

