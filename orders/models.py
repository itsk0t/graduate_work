from django.db import models
from auth.models import CustomUser
from products.models import Products
from technical.models import UserAddress


class Order(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, verbose_name='Адрес')
    comment = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
