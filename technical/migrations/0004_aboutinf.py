# Generated by Django 4.1.3 on 2024-05-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0003_contactinf'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Информация',
            },
        ),
    ]