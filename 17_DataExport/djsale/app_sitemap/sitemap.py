from django.contrib.sitemaps import Sitemap
from app_news.models import NewsItem
from django.urls import reverse


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return NewsItem.objects.filter(is_published=True)

    def lastmod(self, obj: NewsItem):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['about_list', 'contacts']

    def location(self, item):
        return reverse(item)
