from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from auth.models import CustomUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Логин'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Имя'}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Номер телефона'}))
    date_birth = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Дата рождения'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control w-75', 'placeholder': 'Email-адрес'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'phone_number', 'date_birth', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder':'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder':'Пароль'}))