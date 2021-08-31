from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Item, ItemInstance

from django.db import connection, reset_queries


class ItemListView(ListView):
    queryset = Item.objects.select_related('shop').all()
    context_object_name = 'items'

    # for query in queryset:
    #     print(query, query.shop)
    # print('количество запросов', len(connection.queries))
    # reset_queries()


class ItemDetailView(View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        return render(request, 'app_goods/item_detail.html', {'item': item})

    def post(self, request, pk):
        user = request.user
        item = Item.objects.get(pk=pk)
        print('добавляем в корзину', item)

        item_instance = ItemInstance.objects.filter(item=item).first()
        item_instance.buyer_pk = user.pk
        item_instance.status = 'в корзине'
        item.number_on_sale -= 1
        item_instance.save()
        item.save()

        return HttpResponseRedirect(reverse('items'))
