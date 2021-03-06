from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='фамилия')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class ProfileForm(forms.Form):
    add_to_balance = forms.DecimalField(help_text='добавить к балансу')
