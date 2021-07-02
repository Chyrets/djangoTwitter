from django.contrib.auth.models import User

from content.models import Post


def show_all_user_post(user: User) -> Post:
    """Показать все посты пользователя"""
    return Post.objects.filter(author=user)
