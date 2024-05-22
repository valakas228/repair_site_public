from django.core.management.base import BaseCommand
from ...models import Category, PriceList


class Command(BaseCommand):
    help = 'Adds price list entries for categories'

    def handle(self, *args, **kwargs):
        categories = [
            {'name': 'Смартфоны', 'slug': 'smartphones', 'description': 'Ремонт и обслуживание смартфонов'},
            {'name': 'Планшеты', 'slug': 'tablets', 'description': 'Ремонт и обслуживание планшетов'},
            {'name': 'Ноутбуки', 'slug': 'laptops', 'description': 'Ремонт и обслуживание ноутбуков'},
            {'name': 'Компьютеры', 'slug': 'computers', 'description': 'Ремонт и обслуживание компьютеров'},
            {'name': 'Телевизоры', 'slug': 'tvs', 'description': 'Ремонт и обслуживание телевизоров'},
            {'name': 'Аудио и Видео техника', 'slug': 'audio-video', 'description': 'Ремонт аудио и видео техники'},
            {'name': 'Игровые консоли', 'slug': 'gaming-consoles', 'description': 'Ремонт игровых консолей'},
            {'name': 'Умные устройства', 'slug': 'smart-devices', 'description': 'Ремонт умных устройств'},
            {'name': 'Принтеры и сканеры', 'slug': 'printers-scanners', 'description': 'Ремонт принтеров и сканеров'},
            {'name': 'Аксессуары', 'slug': 'accessories', 'description': 'Ремонт и обслуживание аксессуаров'},
        ]

        for category_data in categories:
            category, _ = Category.objects.get_or_create(slug=category_data['slug'], defaults=category_data)
            PriceList.objects.create(category=category, repair_type='Тип ремонта', price=100.00)

        self.stdout.write(self.style.SUCCESS('Price list entries added successfully'))
