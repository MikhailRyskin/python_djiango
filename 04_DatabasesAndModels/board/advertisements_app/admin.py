from django.contrib import admin
from .models import Advertisement, AdvertisementAuthor, AdvertisementRubric


# Register your models here.

# @admin.register(Advertisement, AdvertisementAuthor, AdvertisementRubric)
# class AdvertisementAdmin(admin.ModelAdmin):
#     pass

# class AdvertisementInline(admin.TabularInline):
#     model = Advertisement


class AdvertisementAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    # inlines = ['AdvertisementInline']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rubric')
    search_fields = ['description']
    list_filter = ['author']


# admin.site.register(Advertisement)
admin.site.register(AdvertisementAuthor, AdvertisementAuthorAdmin)
admin.site.register(AdvertisementRubric)
