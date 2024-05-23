from django.db import models

from auth.models import CustomUser


class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class UserAddress(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    street = models.CharField(verbose_name='Улица', max_length=128)
    house = models.CharField(verbose_name='Дом', max_length=3)
    entrance = models.CharField(verbose_name='Подъезд', max_length=3)
    floor = models.CharField(verbose_name='Этаж', max_length=3)
    apartment = models.CharField(verbose_name='Квартира', max_length=3)

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Point(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    area = models.CharField(verbose_name='Район', max_length=32)
    address = models.CharField(verbose_name='Адрес', max_length=256)
    time_delivery = models.CharField(verbose_name='Время доставки', max_length=64)
    time_pickup = models.CharField(verbose_name='Время самовывоз', max_length=64)
    stop = models.BooleanField(verbose_name='Работает/Не работает', default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Точка в гроде'
        verbose_name_plural = 'Точки в городе'


class ContactInf(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=32)
    email = models.CharField(verbose_name='Email-адрес', max_length=128)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакстная информация'
        verbose_name_plural = 'Контакстная информация'


class AboutInf(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

