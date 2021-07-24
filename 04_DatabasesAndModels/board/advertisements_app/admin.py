from django.contrib import admin
from .models import Advertisement, AdvertisementAuthor, AdvertisementRubric


# Register your models here.
@admin.register(Advertisement, AdvertisementAuthor, AdvertisementRubric)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
