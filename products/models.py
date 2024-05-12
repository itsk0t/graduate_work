from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Promotion(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    discount_percentage = models.IntegerField(verbose_name='Процент скиндки (если есть)', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Products(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    price = models.IntegerField(verbose_name='Цена')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE, verbose_name='Акция', default=1)
    stop = models.BooleanField(verbose_name='Находится ли в продаже', default=True)
    nutritional_value = models.CharField(verbose_name='Пищевая ценность', max_length=128)
    mass = models.CharField(verbose_name='Масса', max_length=11, null=True, blank=True)
    volume = models.CharField(verbose_name='Объем', max_length=11, null=True, blank=True)
    quantity = models.CharField(verbose_name='Количество', max_length=11, null=True, blank=True)
    diameter = models.CharField(verbose_name='Диаметр', max_length=11, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'