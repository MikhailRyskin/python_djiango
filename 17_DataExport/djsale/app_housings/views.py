from django.views import generic
from app_housings.models import Housing


class HousingList(generic.ListView):
    queryset = Housing.objects.only('title')


class HousingDetailView(generic.DetailView):
    model = Housing

