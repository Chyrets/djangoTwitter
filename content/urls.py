from django.urls import path

from . import views

urlpatterns = [
    path('my-posts/', views.MyPostsView.as_view(), name='my_post')
]
