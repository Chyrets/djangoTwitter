from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель поста"""
    text = models.TextField(verbose_name='Текст поста', max_length=256)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Автор поста', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
