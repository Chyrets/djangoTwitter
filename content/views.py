from django.shortcuts import render
from django.views import View

from content.serveces.view_services import show_all_user_post


class MyPostsView(View):
    """Страница с потсами пользователя"""
    template_name = 'content/user_posts.html'

    def get(self, request):
        user = request.user
        posts = show_all_user_post(user)

        context = {
            'posts': posts
        }

        return render(request, self.template_name, context)
