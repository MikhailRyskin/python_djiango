from django.contrib import admin
from .models import Shop, Item, ItemInstance


class ShopAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')


class ItemAdmin(admin.ModelAdmin):
    fields = ( 'shop', 'name', 'description', 'price', 'number_on_sale')
    list_display = ('id', 'name', 'price', 'number_on_sale', 'number_of_sold')


class ItemInstanceAdmin(admin.ModelAdmin):
    fields = ('item',)
    list_display = ('id', 'item', 'status', 'date_of_sale')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemInstance, ItemInstanceAdmin)

