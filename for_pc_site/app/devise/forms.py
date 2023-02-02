from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'reg-input',
                'placeholder': 'имя'
            }),
            'email': TextInput(attrs={
                'class': 'reg-input',
                'placeholder': 'ел почта'
            }),
            'password1': TextInput(attrs={
                'class': 'reg-input',
                'placeholder': 'пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'reg-input',
                'placeholder': 'повторный пароль'
            }),
        }