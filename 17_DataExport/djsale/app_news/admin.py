from django.contrib import admin
from app_news.models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(NewsItem, NewsItemAdmin)
