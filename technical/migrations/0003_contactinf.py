# Generated by Django 4.1.3 on 2024-05-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0002_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32, verbose_name='Телефон')),
                ('email', models.CharField(max_length=128, verbose_name='Email-адрес')),
            ],
            options={
                'verbose_name': 'Контакстная информация',
                'verbose_name_plural': 'Контакстная информация',
            },
        ),
    ]
