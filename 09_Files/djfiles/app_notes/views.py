from datetime import datetime
from _csv import reader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.utils.translation import gettext as _
from app_notes.forms import NoteForm, UploadNotesForm
from app_notes.models import Note, NoteImage


@login_required(login_url='/users/login')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            text = form.cleaned_data['text']
            note = Note.objects.create(user=user, text=text)
            images = request.FILES.getlist('file_field')
            for img in images:
                image = NoteImage(note=note, image=img)
                image.save()
            return redirect(reverse('notes'))
    else:
        form = NoteForm()
    return render(request, 'app_notes/note_form.html', {'form': form})


def note_list(request):
    notes = Note.objects.order_by('-created_date')
    for note in notes:
        if len(note.text) > 30:
            note.text = f'{note.text[:27]}...'
    return render(request, 'app_notes/note_list.html', {'notes': notes})


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        note_id = int(self.kwargs['pk'])
        context['images'] = NoteImage.objects.all().filter(note=note_id)
        return context


@login_required(login_url='/users/login')
def load_notes(request):
    if request.method == 'POST':
        upload_file_form = UploadNotesForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            notes_file = upload_file_form.cleaned_data['file'].read()
            notes_str = notes_file.decode('utf-8').split('\n')
            csv_reader = reader(notes_str, delimiter=";", quotechar='"')
            for row in csv_reader:
                Note.objects.create(user=request.user, text=row[0],
                                    publication_date=datetime.strptime(row[1], "%d.%m.%Y"))
            return HttpResponse(content=_('Notes entered into the database'), status=200)
    else:
        upload_file_form = UploadNotesForm()
    context = {
        'form': upload_file_form
    }
    return render(request, 'app_notes/upload_notes.html', context=context)
