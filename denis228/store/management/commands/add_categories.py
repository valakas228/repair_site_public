from django.core.management.base import BaseCommand
from store.models import Category

class Command(BaseCommand):
    help = 'Добавляет категории товаров в базу данных'

    def handle(self, *args, **options):
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
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                slug=category_data['slug'],
                defaults={'description': category_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Категория '{category.name}' была успешно создана."))
            else:
                self.stdout.write(self.style.WARNING(f"Категория '{category.name}' уже существует."))
