# Generated by Django 5.0.7 on 2024-08-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_alter_car_brand_alter_car_factory_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
