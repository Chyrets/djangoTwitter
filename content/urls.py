from django.urls import path

from . import views

urlpatterns = [
    path('posts/<username>/', views.UserPostsView.as_view(), name='user_posts'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='post'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
]
