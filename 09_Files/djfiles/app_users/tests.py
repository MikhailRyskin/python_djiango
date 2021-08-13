from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

USERNAME = 'test_user_1'
FIRST_NAME = 'test_first_name_1'
LAST_NAME = 'test_last_name_1'
PASSWORD = 'test@!password_1'
ABOUT = 'test text about user'


class TestRegister(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test_user',
                                        first_name='test_first_name',
                                        last_name='test_last_name',
                                        password='12345'
                                        )
        Profile.objects.create(user=user, about='text about user')

    def test_account_view(self):
        url = reverse('account', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')
        self.assertContains(response, 'test_first_name')
        self.assertContains(response, 'text about user')

    def test_register_exists_at_desired_location(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_post(self):
        url = reverse('register')
        response = self.client.post(url,
                                    {'username': USERNAME,
                                     'first_name': FIRST_NAME,
                                     'last_name': LAST_NAME,
                                     'about': ABOUT,
                                     'password1': PASSWORD,
                                     'password2': PASSWORD
                                     })
        new_user = User.objects.get(username=USERNAME)
        self.assertEqual(new_user.first_name, FIRST_NAME)
        self.assertEqual(new_user.last_name, LAST_NAME)
        new_user_profile = Profile.objects.get(user=new_user)
        self.assertEqual(new_user_profile.about, ABOUT)

    def test_account_edit_unauthorized_user(self):
        url = reverse('account_edit', args=[1])
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_account_edit_get(self):
        self.client.login(username='test_user', password='12345')
        url = reverse('account_edit', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update_form.html')

    def test_account_edit_post(self):
        self.client.login(username='test_user', password='12345')
        edit_user = User.objects.get(username='test_user')
        self.assertEqual(edit_user.first_name, 'test_first_name')
        url = reverse('account_edit', args=[1])
        response = self.client.post(url,
                                    {'first_name': 'new_name'})
        self.assertRedirects(response, reverse('notes'))
        edit_user.refresh_from_db()
        self.assertEqual(edit_user.first_name, 'new_name')
