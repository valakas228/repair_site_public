from django.contrib import admin
from .models import Category, Product, ProductAttribute, RepairService, Comment, Cart, CartItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(RepairService)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(CartItem)
