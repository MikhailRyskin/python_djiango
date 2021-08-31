from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Profile
from app_goods.models import ItemInstance
from .forms import RegisterForm, ProfileForm
from app_users.users_utils import increase_balance


def register_view(request):
    if request.method == 'POST':
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
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


class AccountDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'


def balance_view(request, *args, **kwargs):
    if request.method == 'POST':
        user = request.user
        form = ProfileForm(request.POST)
        if form.is_valid():
            add_to_balance = form.cleaned_data.get('add_to_balance')
            profile = Profile.objects.get(user=user)
            increase_balance(profile, add_to_balance)
            return redirect('account', pk=user.id)
    else:
        form = ProfileForm()
    return render(request, 'users/balance_form.html', {'form': form})


class CartView(View):
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
        print('совершаем покупку', user.username)
        # user = request.user
        # item = Item.objects.get(pk=pk)
        # print('добавляем в корзину', item)
        #
        # item_instance = ItemInstance.objects.filter(item=item).first()
        # item_instance.buyer_pk = user.pk
        # item_instance.status = 'в корзине'
        # item.number_on_sale -= 1
        # item_instance.save()
        # item.save()

        return HttpResponseRedirect(reverse('items'))
