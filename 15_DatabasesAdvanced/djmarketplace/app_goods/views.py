from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Item, ItemInstance


class ItemListView(ListView):
    queryset = Item.objects.filter(number_on_sale__gt=0).only('name', 'shop').select_related('shop')
    context_object_name = 'items'


class ItemDetailView(View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        return render(request, 'app_goods/item_detail.html', {'item': item})

    def post(self, request, pk):
        user = request.user
        item = Item.objects.get(pk=pk)
        # добавление экземпляра товара в корзину пользователя
        with transaction.atomic():
            item_instance = ItemInstance.objects.filter(item=item, status='в продаже').first()
            item_instance.status = 'в корзине'
            item_instance.buyer_pk = user.pk
            item_instance.save()
            item.number_on_sale -= 1
            item.save()

        return HttpResponseRedirect(reverse('items'))
