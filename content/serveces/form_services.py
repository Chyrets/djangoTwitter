from django.contrib.auth.models import User

from content.models import Post


def create_new_post(text: str, user: User) -> Post:
    """Создать новый пост"""
    return Post.objects.create(text=text, author=user)
