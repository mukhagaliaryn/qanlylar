from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Тема', max_length=255)
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='main/posts/')
    about = models.TextField(verbose_name='О статье', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)
    is_public = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class News(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Тема', max_length=255)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)
    is_public = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Person(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=64)
    specialist = models.CharField(verbose_name='Специальность', max_length=64)
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='main/persons/')
    about = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Лица'


class Gallery(models.Model):
    image = models.FileField(verbose_name='Галерея', blank=True, null=True, upload_to='main/gallery/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Тема', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


