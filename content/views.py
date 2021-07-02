from django.shortcuts import render
from django.views import View

from content.serveces.view_services import show_all_user_post, show_post


class MyPostsView(View):
    """Страница с потсами авторизованного пользователя"""
    template_name = 'content/user_posts.html'

    def get(self, request):
        user = request.user
        posts = show_all_user_post(user)

        context = {
            'posts': posts
        }

        return render(request, self.template_name, context)


class PostView(View):
    """Страница с полной информацией об посте"""
    template_name = 'content/post.html'

    def get(self, request, post_id):
        post = show_post(post_id)

        context = {
            'post': post
        }

        return render(request, self.template_name, context)
