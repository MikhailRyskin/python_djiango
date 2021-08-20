from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('first name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('last name'))

    balance = forms.IntegerField(required=False, help_text=_('balance'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
