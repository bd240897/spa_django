from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# наследуем его от класса Form
class SigUpForm(forms.Form):
    """Форма для логина"""

    # поля формы и их классы

    username = forms.CharField(
        max_length=100,
        required=True,
        # Виджет – это представление поля в виде HTML кода.
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        """Метод для валидации форм. """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        # проверка совпадений паролей
        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        """Метод сохранение данных формы в базу данных"""

        # сохраняет в БД пользователя - НЕТ проверки что пользователь уже есть
        if not User.objects.filter(username=self.cleaned_data['username']).exists():
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
            )
            user.save()
        # Если такой пользователь есть, то метод authenticate возвращает нам объект User
        auth = authenticate(**self.cleaned_data)
        return auth

class SignInForm(forms.Form):
    """Форма входа"""
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )