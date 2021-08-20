from django.contrib import admin
from .models import Promotion, Shop, Offer, Purchase


class ShopAdmin(admin.ModelAdmin):
    fields = ('shop_name',)
    list_display = ('shop_name',)


class PromotionAdmin(admin.ModelAdmin):
    fields = ('promotion',)
    list_display = ('promotion',)


class OfferAdmin(admin.ModelAdmin):
    fields = ('user', 'offer')
    list_display = ('user', 'offer')


class PurchaseAdmin(admin.ModelAdmin):
    fields = ('user', 'purchase')
    list_display = ('user', 'purchase')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Purchase, PurchaseAdmin)

