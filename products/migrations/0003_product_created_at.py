# Generated by Django 4.0 on 2022-01-02 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_amount_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 1, 2, 8, 29, 38, 760521, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
