from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('first name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('last name'))

    about = forms.CharField(max_length=1000, widget=forms.Textarea, required=False, help_text=_('about'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
