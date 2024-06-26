# Generated by Django 4.1.3 on 2024-05-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=32, verbose_name='Район')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес')),
                ('time_delivery', models.CharField(max_length=64, verbose_name='Время доставки')),
                ('time_pickup', models.CharField(max_length=64, verbose_name='Время самовывоз')),
                ('stop', models.BooleanField(default=True, verbose_name='Работает/Не работает')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technical.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Точка в гроде',
                'verbose_name_plural': 'Точки в городе',
            },
        ),
    ]
