# Generated by Django 4.2.7 on 2024-05-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='89bb92_iphone-14-pro-small.jpeg', upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]