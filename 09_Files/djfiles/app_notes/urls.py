from django.urls import path
from .views import create_note, note_list, NoteDetailView, load_notes


urlpatterns = [
    path('', note_list, name='notes'),
    path('<int:pk>', NoteDetailView.as_view(), name='note_detail'),
    path('create', create_note, name='create_note'),
    path('load_notes', load_notes, name='load_notes')
    ]
