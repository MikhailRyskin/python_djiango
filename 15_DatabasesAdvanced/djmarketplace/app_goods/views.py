import logging
from time import asctime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.db.models import Count, Q
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Item, ItemInstance
from .forms import PeriodForm

logger = logging.getLogger(__name__)


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

        logger.info(f'{asctime()} user:{user.username} added to cart {item.name}')
        return HttpResponseRedirect(reverse('items'))


class StatisticsView(View):
    def get(self, request):
        form = PeriodForm()
        return render(request, 'app_goods/period_form.html', {'form': form})

    def post(self, request):
        form = PeriodForm(request.POST)
        if form.is_valid():
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            # items = Item.objects.annotate(total_sales=Count('instances')).order_by('-total_sales')
            items = Item.objects.annotate(total_sales=Count('instances',
                                                        filter=Q(instances__status='продано',
                                                        instances__date_of_sale__gte=date_from,
                                                        instances__date_of_sale__lte=date_to))).order_by('-total_sales')
            return render(request, 'app_goods/period_statistics.html', {'date_from': date_from, 'date_to': date_to,
                                                                        'items': items})
        return render(request, 'app_goods/period_form.html', {'form': form})
