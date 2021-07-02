from django import forms
from django.contrib.auth.models import User

from account.serveces.form_services import unique_username, unique_email


class SignupForm(forms.ModelForm):
    """Форма для регистрации пользователя"""
    username = forms.CharField(widget=forms.TextInput(), max_length=17, required=True)
    email = forms.CharField(widget=forms.EmailInput(), max_length=17, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(unique_username)
        self.fields['email'].validators.append(unique_email)
