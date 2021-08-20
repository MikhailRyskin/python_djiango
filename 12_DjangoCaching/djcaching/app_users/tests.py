from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import Profile
from app_purchases.models import Promotion, Offer, Purchase

NUMBER_OF_PROMOTIONS = 8
NUMBER_OF_OFFERS = 5
NUMBER_OF_PURCHASES = 3


class TestAccount(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_1 = User.objects.create_user(username='test_user_1',
                                          first_name='test_first_name_1',
                                          last_name='test_last_name_1',
                                          password='123451'
                                          )
        Profile.objects.create(user=user_1, balance=15)
        user_2 = User.objects.create_user(username='test_user_2',
                                          first_name='test_first_name_2',
                                          last_name='test_last_name_2',
                                          password='1234512'
                                          )
        Profile.objects.create(user=user_2, balance=25)

        for promotion_index in range(1, NUMBER_OF_PROMOTIONS + 1):
            Promotion.objects.create(
                promotion=f'акция:{promotion_index}',
            )

        for offer_index in range(1, NUMBER_OF_OFFERS + 1):
            Offer.objects.create(
                user=user_1,
                offer=f'предложение:{offer_index}',
            )

        for purchase_index in range(1, NUMBER_OF_PURCHASES + 1):
            Purchase.objects.create(
                user=user_1,
                purchase=f'покупка:{purchase_index}',
            )

    def test_account_view_unauthorized_user(self):
        url = reverse('account', args=[1])
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_account_view_another_authorized_user(self):
        self.client.login(username='test_user_1', password='123451')
        url = reverse('account', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('No access to account'))

    def test_account_view(self):
        self.client.login(username='test_user_1', password='123451')
        url = reverse('account', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')
        self.assertContains(response, 'test_user')
        self.assertContains(response, '15')
        for promotion_index in range(1, NUMBER_OF_PROMOTIONS + 1):
            self.assertContains(response, f'акция:{promotion_index}')
        for offer_index in range(1, NUMBER_OF_OFFERS + 1):
            self.assertContains(response, f'предложение:{offer_index}')
        for purchase_index in range(1, NUMBER_OF_PURCHASES + 1):
            self.assertContains(response, f'покупка:{purchase_index}')


class TestRegister(TestCase):
    def test_register_exists_at_desired_location(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_post(self):
        self.assertEqual(User.objects.count(), 0)
        url = reverse('register')
        response = self.client.post(url,
                                    {'username': 'test_user_3',
                                     'first_name': 'test_first_name_3',
                                     'last_name': 'test_last_name_3',
                                     'balance': '22',
                                     'password1': 'test@!password_1',
                                     'password2': 'test@!password_1'
                                     })
        self.assertEqual(User.objects.count(), 1)
        new_user = User.objects.get(username='test_user_3')
        self.assertEqual(new_user.first_name, 'test_first_name_3')
        self.assertEqual(new_user.last_name, 'test_last_name_3')
        new_user_profile = Profile.objects.get(user=new_user)
        self.assertEqual(new_user_profile.balance, 22)
        self.assertRedirects(response, reverse('account', args=[1]))
