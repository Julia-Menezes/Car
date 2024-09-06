# Generated by Django 5.0.7 on 2024-08-06 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='Cars.brand'),
        ),
    ]
