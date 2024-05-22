from django.core.management.base import BaseCommand
from ...models import Product, RepairService

class Command(BaseCommand):
    help = 'Add initial repair services'

    def handle(self, *args, **kwargs):
        # Найдём товары, для которых будем добавлять услуги
        try:
            iphone = Product.objects.get(slug='iphone-14')
            galaxy = Product.objects.get(slug='samsung-galaxy-s21')
            headphones = Product.objects.get(slug='sony-wh-1000xm4')
        except Product.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Product does not exist: {str(e)}"))
            return

        repair_services_data = [
            # Услуги для iPhone 14
            {
                'device': iphone,
                'service_name': 'Screen Replacement',
                'description': 'Replacement of the iPhone 14 screen.',
                'price': 199.99,
                'estimated_time': '1 hour'
            },
            {
                'device': iphone,
                'service_name': 'Battery Replacement',
                'description': 'Replacement of the iPhone 14 battery.',
                'price': 99.99,
                'estimated_time': '30 minutes'
            },
            {
                'device': iphone,
                'service_name': 'Camera Repair',
                'description': 'Repair of the iPhone 14 camera.',
                'price': 149.99,
                'estimated_time': '1.5 hours'
            },
            # Добавьте остальные услуги здесь...
            # Услуги для Samsung Galaxy S21
            {
                'device': galaxy,
                'service_name': 'Screen Replacement',
                'description': 'Replacement of the Samsung Galaxy S21 screen.',
                'price': 179.99,
                'estimated_time': '1 hour'
            },
            # Добавьте остальные услуги здесь...
            # Услуги для Sony WH-1000XM4
            {
                'device': headphones,
                'service_name': 'Ear Pad Replacement',
                'description': 'Replacement of the ear pads on Sony WH-1000XM4.',
                'price': 49.99,
                'estimated_time': '20 minutes'
            },
            # Добавьте остальные услуги здесь...
        ]

        for service_data in repair_services_data:
            service = RepairService.objects.create(**service_data)
            self.stdout.write(self.style.SUCCESS(f"Successfully added repair service: {service.service_name}"))
