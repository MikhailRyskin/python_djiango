from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Shop(models.Model):
    shop_name = models.TextField(null=True, blank=True, verbose_name=_('shop_name'))

    class Meta:
        verbose_name_plural = _('shops')
        verbose_name = _('shop')


class Promotion(models.Model):
    promotion = models.TextField(null=True, blank=True, verbose_name=_('promotion'))

    class Meta:
        verbose_name_plural = _('promotions')
        verbose_name = _('promotion')


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    offer = models.TextField(null=True, blank=True, verbose_name=_('offer'))

    class Meta:
        verbose_name_plural = _('offers')
        verbose_name = _('offer')


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    purchase = models.TextField(null=True, blank=True, verbose_name=_('purchase'))

    class Meta:
        verbose_name_plural = _('purchases')
        verbose_name = _('purchase')
