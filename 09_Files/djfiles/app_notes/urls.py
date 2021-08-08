from django.urls import path
from .views import create_note, NoteListView, NoteDetailView, load_notes


urlpatterns = [
    path('', NoteListView.as_view(), name='notes'),
    path('<int:pk>', NoteDetailView.as_view(), name='note_detail'),
    path('create', create_note, name='create_note'),
    path('load_notes', load_notes, name='load_notes')
    ]
