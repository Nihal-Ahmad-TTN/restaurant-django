# Generated by Django 5.1.6 on 2025-03-12 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_orders_ordered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ordered_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 7, 29, 3, 401986, tzinfo=datetime.timezone.utc)),
        ),
    ]
