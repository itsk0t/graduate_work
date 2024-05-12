from django.db import models

from auth.models import CustomUser


class Comments(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст отзыва')
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    status = models.BooleanField(verbose_name='Опубликован или нет', default=False)

    def __str__(self):
        return self.user_id.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

