# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
# from django.http import HttpResponse
# from django.shortcuts import render
# from .forms import AuthForm


# Create your views here.
class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'
    # next_page = '/about'
