from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def unique_username(username: str):
    """Проверка имени пользователя на существование в БД"""
    if User.objects.filter(username__iexact=username).exists():
        raise ValidationError('Пользователь с таким именем уже существует.')


def unique_email(email: str):
    """Проверка почты на существование в БД"""
    if User.objects.filter(email__exact=email):
        raise ValidationError("Пользователь с такой почтой уже существует")
