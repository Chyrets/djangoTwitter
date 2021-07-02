from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from account.forms import SignupForm
from account.serveces.view_serveces import create_new_user


class LoginUser(View):
    """Страница для авторизации пользователя"""
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        return render(request, self.template_name)


class SignupView(View):
    """Отображение страницы для регистрации пользователя"""
    form_class = SignupForm
    template_name = 'account/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = create_new_user(username, email, password)

            if user is not None:
                login(request, user)

        return redirect('/')
