from django.db import models
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/', blank=True)
    image_url = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            response = requests.get(self.image_url)
            if response.status_code == 200:
                image_name = self.image_url.split("/")[-1]
                self.image.save(image_name, ContentFile(response.content), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product} - {self.name}: {self.value}"


class RepairService(models.Model):
    device = models.ForeignKey(Product, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    estimated_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.device.name} - {self.service_name}"


class Comment(models.Model):
    product = models.ForeignKey('Product', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.created_at}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return "Cart for anonymous user"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"
