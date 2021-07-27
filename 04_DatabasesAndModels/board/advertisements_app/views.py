from django.db.models import F
from django.views import generic
from .models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisements'
    # queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get_object(self, queryset=None):
        obj = super().get_object()
        # obj.views_count += 1
        obj.views_count = F('views_count') + 1
        obj.save()
        obj.refresh_from_db()
        return obj

