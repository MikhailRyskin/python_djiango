from django.views import generic
from .models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisements'
    # queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
