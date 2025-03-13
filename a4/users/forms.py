from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
       label='Логин'
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Имя',
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Фамилия',
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label='Почта',
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
            field.widget.attrs['placeholder'] = field.label


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин'
    )

    class Meta:
        model = User
        fields = ('username', 'password1')

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
            field.widget.attrs['placeholder'] = field.label