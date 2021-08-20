from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Profile
from app_purchases.models import Promotion, Offer, Purchase
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            balance = form.cleaned_data.get('balance')
            Profile.objects.create(
                user=user,
                balance=balance,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('account', pk=user.id)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'


@login_required
def account_view(request, *args, **kwargs):
    if request.user.id == kwargs['pk']:
        user = request.user
        promotions = Promotion.objects.all()
        offers = Offer.objects.all().filter(user=user)
        username = user.username
        promotions_cache_key = f'promotions:{username}'
        offers_cache_key = f'offers:{username}'
        cache.get_or_set(promotions_cache_key, promotions, 30*60)
        cache.get_or_set(offers_cache_key, offers, 30*60)
        purchases = Purchase.objects.all().filter(user=user)
        return render(request, 'users/user_detail.html',
                      {'user': user, 'promotions': promotions, 'offers': offers, 'purchases': purchases})
    else:
        return HttpResponse(content=_('No access to account'), status=200)
