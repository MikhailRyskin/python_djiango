from django.views.generic import ListView
from .models import Shop


class ShopListView(ListView):
    model = Shop
    context_object_name = 'shops'
