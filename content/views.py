from django.shortcuts import render, redirect
from django.views import View

from content.forms import AddPostForm
from content.serveces.form_services import create_new_post
from content.serveces.view_services import show_post, show_all_user_posts


class UserPostsView(View):
    """Страница с постами пользователя"""
    template_name = 'content/user_posts.html'

    def get(self, request, username):
        posts = show_all_user_posts(username)

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


class AddPostView(View):
    """Страница на которой можно создать пост"""
    form_class = AddPostForm
    template_name = 'content/add_post.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        user = request.user

        if form.is_valid():
            text = form.cleaned_data.get('text')
            post = create_new_post(text, user)
            return redirect('my_post')

        return render(request, self.template_name)
