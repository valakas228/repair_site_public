# Generated by Django 4.2.7 on 2024-06-11 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_repairrequest_response'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RepairRequest',
        ),
    ]