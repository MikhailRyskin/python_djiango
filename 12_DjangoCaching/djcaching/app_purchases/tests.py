from django.test import TestCase
from django.urls import reverse
from .models import Shop


NUMBER_OF_SHOPS = 10


class ShopListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for shop_index in range(1, NUMBER_OF_SHOPS + 1):
            Shop.objects.create(
                shop_name=f'магазин:{shop_index}',
            )

    def test_shop_list_view(self):
        url = reverse('shops')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_purchases/shop_list.html')
        self.assertTrue(len(response.context['shops']) == NUMBER_OF_SHOPS)
        for shop_index in range(1, NUMBER_OF_SHOPS + 1):
            self.assertContains(response, f'магазин:{shop_index}')
