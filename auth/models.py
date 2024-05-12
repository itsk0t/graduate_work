from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
