from django.contrib.auth.models import User


def create_new_user(username: str, email: str, password: str) -> User:
    """Создание нового пользователя"""
    return User.objects.create_user(username=username, email=email, password=password)

