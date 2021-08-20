from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Note, NoteImage

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

class NoteCreateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        note_1 = Note.objects.create(
            user=test_user1,
            text=f'какой-то текст')

    def test_note_create_get(self):
        self.client.login(username='testuser1', password='12345')
        url = reverse('create_note')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_notes/note_form.html')

    def test_note_create_post(self):
        test_image_1 = SimpleUploadedFile("test_photo_1.jpg", b"file_content", content_type="image")
        test_image_2 = SimpleUploadedFile("test_photo_2.jpg", b"file_content", content_type="image")
        self.client.login(username='testuser1', password='12345')
        url = reverse('create_note')
        response = self.client.post(url,
                                    {'text': 'новый текст заметки',
                                     'file_field': [test_image_1, test_image_2]})
        self.assertRedirects(response, reverse('notes'))
        new_note = Note.objects.get(id=2)
        self.assertEqual(new_note.text, 'новый текст заметки')
        self.assertEqual(len(NoteImage.objects.all()), 2)
        self.assertEqual(NoteImage.objects.get(id=2).note, new_note)


class LoadNotesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        note_1 = Note.objects.create(
            user=test_user1,
            text=f'заметка 1')

    def test_load_notes_get(self):
        self.client.login(username='testuser1', password='12345')
        url = reverse('load_notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_notes/upload_notes.html')

    def test_load_notes_POST(self):
        self.client.login(username='testuser1', password='12345')
        url = reverse('load_notes')
        self.assertEqual(len(Note.objects.all()), 1)
        with open('app_notes/test_csv.csv', encoding='utf-8') as test_csv_file:
            response = self.client.post(url,
                                        {'file': test_csv_file})
        self.assertEqual(len(Note.objects.all()), 3)
        note_2 = Note.objects.get(id=2)
        self.assertEqual(note_2.text, 'это заметка 2')
        note_3 = Note.objects.get(id=3)
        self.assertEqual(note_3.text, 'следующая тестовая заметка')
