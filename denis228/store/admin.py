from django.contrib import admin
from .models import Category, Product, ProductAttribute, RepairService
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductAttribute)
admin.site.register(RepairService)