from django import forms


class NoteForm(forms.Form):
    text = forms.CharField(max_length=2000, widget=forms.Textarea, help_text='текст заметки')
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class UploadNotesForm(forms.Form):
    file = forms.FileField()
