from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    email = forms.EmailField(max_length=30, required=False, help_text='e-mail')

    phone = forms.CharField(max_length=12, required=False, help_text='телефон')
    city = forms.CharField(max_length=36, required=False, help_text='город')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password1']
