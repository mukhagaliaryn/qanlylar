from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Тема', max_length=255, default='')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)
    is_public = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
