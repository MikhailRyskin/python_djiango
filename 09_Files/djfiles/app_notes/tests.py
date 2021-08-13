from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Note

NUMBER_OF_ITEMS = 5


class NotesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for item_index in range(1, NUMBER_OF_ITEMS + 1):
            Note.objects.create(
                user=User.objects.create(username=f'user_{item_index}'),
                text=f'какой-то текст {item_index} ещё текст',
            )

    def test_notes_view(self):
        url = reverse('notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_notes/note_list.html')
        self.assertTrue(len(response.context['notes']) == NUMBER_OF_ITEMS)

    def test_detail_note_view(self):
        for item_index in range(1, NUMBER_OF_ITEMS + 1):
            url = reverse('note_detail', args=[item_index])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'app_notes/note_detail.html')
            self.assertContains(response, f'какой-то текст {item_index} ещё текст')


class NotesCreateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        note_1 = Note.objects.create(
            user=test_user1,
            text=f'какой-то текст')

    def test_notes_create_get(self):
        self.client.login(username='testuser1', password='12345')
        url = reverse('create_note')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_notes/note_form.html')

    def test_notes_create_post(self):
        self.client.login(username='testuser1', password='12345')
        url = reverse('create_note')
        response = self.client.post(url,
                                    {'text': 'новый текст заметки'})
        self.assertRedirects(response, reverse('notes'))
        new_note = Note.objects.get(id=2)
        self.assertEqual(new_note.text, 'новый текст заметки')
