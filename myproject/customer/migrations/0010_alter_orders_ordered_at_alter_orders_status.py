# Generated by Django 5.1.6 on 2025-03-12 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_orders_ordered_at_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ordered_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 10, 20, 37, 777813, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default='ADDED', max_length=50),
        ),
    ]
