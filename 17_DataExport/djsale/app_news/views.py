from django.views import generic
from app_news.models import NewsItem


class NewsItemList(generic.ListView):
    queryset = NewsItem.objects.only('title')


class NewsItemDetailView(generic.DetailView):
    model = NewsItem
