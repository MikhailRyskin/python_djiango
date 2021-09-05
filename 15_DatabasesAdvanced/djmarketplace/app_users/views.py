import datetime
import logging
from time import asctime

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.db.models import F
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile
from app_goods.models import ItemInstance, Item
from .forms import RegisterForm, ProfileForm
from app_users.users_utils import change_status


logger = logging.getLogger(__name__)


class RegisterView(View):
    def post(self,  request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('account', pk=user.pk)
        return render(request, 'users/register.html', {'form': form})

    def get(self,  request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})


class AccountDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class AnotherLoginView(LoginView):
    # logger.info(f'{asctime()} user authentication')
    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        logger.info(f'{asctime()} user:{self.request.user.username} authentication')
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'


class BalanceView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

    def get(self, request, pk):
        form = ProfileForm()
        return render(request, 'users/balance_form.html', {'form': form})

    def post(self, request, pk):
        user = request.user
        form = ProfileForm(request.POST)
        if form.is_valid():
            #  увеличение баланса пользователя
            add_to_balance = form.cleaned_data.get('add_to_balance')
            user.profile.balance = F('balance') + add_to_balance
            user.profile.save()

            logger.info(f'{asctime()} user:{user.username} refill balance on {add_to_balance}')
            return redirect('account', pk=user.pk)
        return render(request, 'users/balance_form.html', {'form': form})


class CartView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

    def get(self, request, pk):
        user = request.user
        item_instances = ItemInstance.objects.filter(buyer_pk=pk, status='в корзине').select_related('item')
        total_amount = 0
        for instance in item_instances:
            total_amount += instance.item.price
        return render(request, 'users/user_cart.html', {'user': user, 'items': item_instances,
                                                        'total_amount': total_amount})

    def post(self, request, pk):
        user = request.user
        item_instances = ItemInstance.objects.filter(buyer_pk=pk, status='в корзине').select_related('item')
        # покупка всех товаров в корзине пользователя:
        #   изменение статуса экземпляра товара
        #   заполнение даты продажи экземпляра товара
        #   увеличение количества проданных единиц товара
        # уменьшение баланса, увеличение общей суммы покупок на сумму корзины. Изменение статуса.
        with transaction.atomic():
            total_amount = 0
            bought_items = []
            for instance in item_instances:
                instance.status = 'продано'
                instance.date_of_sale = datetime.datetime.now().date()
                instance.item.number_of_sold += 1
                bought_items.append(instance.item)
                total_amount += instance.item.price
            ItemInstance.objects.bulk_update(item_instances, ['status', 'date_of_sale'])
            Item.objects.bulk_update(bought_items, ['number_of_sold'])
            user.profile.balance -= total_amount
            user.profile.amount_purchases += total_amount
            previous_status = user.profile.status
            user.profile.status = change_status(user.profile.amount_purchases)
            user.profile.save()

        logger.info(f'{asctime()} user:{user.username} decrease balance {total_amount}')
        if previous_status != user.profile.status:
            logger.info(f'{asctime()} user:{user.username} change of status to {user.profile.status}')
        return HttpResponseRedirect(reverse('items'))
