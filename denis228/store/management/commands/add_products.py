from django.core.management.base import BaseCommand
from store.models import Category, Product
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Добавляет товары в базу данных'

    def handle(self, *args, **options):
        products = [
            {
                'category_slug': 'smartphones',
                'name': 'iPhone 14 Pro',
                'slug': 'iphone-14-pro',
                'description': 'Новый iPhone 14 Pro с улучшенной камерой и дисплеем.',
                'price': 999.99,
                'image': 'iphone-14-pro-small.jpeg',
                'stock': 10,
                'available': True,
            },
            {
                'category_slug': 'smartphones',
                'name': 'Samsung Galaxy S21',
                'slug': 'samsung-galaxy-s21',
                'description': 'Samsung Galaxy S21 с мощным процессором и камерой.',
                'price': 799.99,
                'image': 'samsung-galaxy-s21.jpeg',
                'stock': 20,
                'available': True,
            },
            {
                'category_slug': 'laptops',
                'name': 'MacBook Pro 16',
                'slug': 'macbook-pro-16',
                'description': 'Мощный MacBook Pro 16 дюймов для профессионалов.',
                'price': 2399.99,
                'image': 'macbook-pro-16.jpeg',
                'stock': 5,
                'available': True,
            },
            {
                'category_slug': 'laptops',
                'name': 'Dell XPS 13',
                'slug': 'dell-xps-13',
                'description': 'Компактный и мощный Dell XPS 13.',
                'price': 1199.99,
                'image': 'dell-xps-13.jpeg',
                'stock': 8,
                'available': True,
            },
            {
                'category_slug': 'tablets',
                'name': 'iPad Pro',
                'slug': 'ipad-pro',
                'description': 'Мощный iPad Pro с поддержкой Apple Pencil.',
                'price': 799.99,
                'image': 'ipad-pro.jpeg',
                'stock': 15,
                'available': True,
            },
            {
                'category_slug': 'tablets',
                'name': 'Samsung Galaxy Tab S7',
                'slug': 'samsung-galaxy-tab-s7',
                'description': 'Samsung Galaxy Tab S7 с ярким дисплеем и стилусом.',
                'price': 649.99,
                'image': 'samsung-galaxy-tab-s7.jpeg',
                'stock': 10,
                'available': True,
            },
            {
                'category_slug': 'accessories',
                'name': 'Apple Watch Series 6',
                'slug': 'apple-watch-series-6',
                'description': 'Apple Watch Series 6 с функцией измерения уровня кислорода в крови.',
                'price': 399.99,
                'image': 'apple-watch-series-6.jpeg',
                'stock': 25,
                'available': True,
            },
            {
                'category_slug': 'accessories',
                'name': 'Samsung Galaxy Buds Pro',
                'slug': 'samsung-galaxy-buds-pro',
                'description': 'Samsung Galaxy Buds Pro с активным шумоподавлением.',
                'price': 199.99,
                'image': 'samsung-galaxy-buds-pro.jpeg',
                'stock': 30,
                'available': True,
            },
        ]

        for product_data in products:
            try:
                category = Category.objects.get(slug=product_data['category_slug'])
                product, created = Product.objects.get_or_create(
                    category=category,
                    name=product_data['name'],
                    slug=product_data['slug'],
                    defaults={
                        'description': product_data['description'],
                        'price': product_data['price'],
                        'image': os.path.join('products', product_data['image']),
                        'stock': product_data['stock'],
                        'available': product_data['available'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Товар '{product.name}' был успешно создан."))
                else:
                    self.stdout.write(self.style.WARNING(f"Товар '{product.name}' уже существует."))
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Категория с slug '{product_data['category_slug']}' не найдена."))
