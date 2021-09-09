from django.contrib.syndication.views import Feed
from django.urls import reverse
from app_news.models import NewsItem


class LatestNewsFeed(Feed):
    title = 'Новости'
    link = '/sitenews'
    description = 'Самые свежие новости'

    def items(self):
        return NewsItem.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('newsitem_detail', args=[item.pk])
