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
