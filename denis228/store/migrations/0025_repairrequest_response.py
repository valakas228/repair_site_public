# Generated by Django 4.2.7 on 2024-06-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_repairrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairrequest',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
