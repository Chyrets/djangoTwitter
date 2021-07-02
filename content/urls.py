from django.urls import path

from . import views

urlpatterns = [
    path('my-posts/', views.MyPostsView.as_view(), name='my_post'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='post')
]
