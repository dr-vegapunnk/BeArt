# Generated by Django 3.2.19 on 2024-08-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20230612_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_images'),
        ),
    ]