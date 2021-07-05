from django import forms

from content.models import Post


class AddPostForm(forms.ModelForm):
    """Форма для создания поста"""

    class Meta:
        model = Post
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
