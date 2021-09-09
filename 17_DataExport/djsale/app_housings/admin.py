from django.contrib import admin
from app_housings.models import RoomsQuantity, HousingType, Housing


class RoomsQuantityAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity']


class HousingTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']


class HousingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


admin.site.register(RoomsQuantity, RoomsQuantityAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(Housing, HousingAdmin)
