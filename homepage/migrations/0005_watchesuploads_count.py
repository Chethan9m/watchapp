# Generated by Django 4.2.13 on 2024-07-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_cart_products_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchesuploads',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]