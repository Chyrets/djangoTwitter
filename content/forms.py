from django import forms

from content.models import Post


class AddPostForm(forms.ModelForm):
    """Форма для создания поста"""

    class Meta:
        model = Post
        fields = ['text']
