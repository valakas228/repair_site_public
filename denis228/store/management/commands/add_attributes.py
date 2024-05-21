from store.models import Category, Product, ProductAttribute

# Создание категории
electronics = Category.objects.create(name='Electronics', slug='electronics', description='Electronic gadgets and devices')

# Создание товаров
products_data = [
    {
        'category': electronics, 'name': 'iPhone 14', 'slug': 'iphone-14', 'description': 'Latest Apple smartphone.',
        'price': 999.99, 'image_url': 'https://example.com/images/iphone-14.jpg', 'stock': 10, 'available': True,
        'attributes': [
            {'name': 'Color', 'value': 'Black'},
            {'name': 'Storage', 'value': '128GB'},
            {'name': 'RAM', 'value': '6GB'}
        ]
    },
    {
        'category': electronics, 'name': 'Samsung Galaxy S21', 'slug': 'samsung-galaxy-s21', 'description': 'Latest Samsung smartphone.',
        'price': 799.99, 'image_url': 'https://example.com/images/galaxy-s21.jpg', 'stock': 15, 'available': True,
        'attributes': [
            {'name': 'Color', 'value': 'White'},
            {'name': 'Storage', 'value': '256GB'},
            {'name': 'RAM', 'value': '8GB'}
        ]
    },
    {
        'category': electronics, 'name': 'Sony WH-1000XM4', 'slug': 'sony-wh-1000xm4', 'description': 'Noise-cancelling headphones.',
        'price': 349.99, 'image_url': 'https://example.com/images/sony-wh-1000xm4.jpg', 'stock': 25, 'available': True,
        'attributes': [
            {'name': 'Color', 'value': 'Black'},
            {'name': 'Battery Life', 'value': '30 hours'},
            {'name': 'Noise Cancelling', 'value': 'Yes'}
        ]
    }
]

for product_data in products_data:
    attributes = product_data.pop('attributes')
    product = Product.objects.create(**product_data)
    for attr in attributes:
        ProductAttribute.objects.create(product=product, **attr)
