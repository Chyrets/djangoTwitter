from django.contrib.auth.models import User

from content.models import Post


def show_all_user_posts(username: str) -> Post:
    """Показать все посты пользователя"""
    user = User.objects.get(username=username)
    return Post.objects.filter(author=user)


def show_post(post_id: int) -> Post:
    """Показать пост по его id"""
    return Post.objects.get(id=post_id)
