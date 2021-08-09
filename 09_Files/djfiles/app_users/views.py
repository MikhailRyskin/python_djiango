from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Profile
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            about = form.cleaned_data.get('about')
            Profile.objects.create(
                user=user,
                about=about,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('account', pk=user.id)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


class AccountDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'


class AccountEditFormView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name')
    template_name = 'users/user_update_form.html'
    pk_url_kwarg = 'pk'
    success_url = '/notes'

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'
