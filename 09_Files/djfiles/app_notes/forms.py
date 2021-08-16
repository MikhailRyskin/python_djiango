from django import forms
from django.utils.translation import gettext_lazy as _


class NoteForm(forms.Form):
    text = forms.CharField(max_length=2000, widget=forms.Textarea, help_text=_('note text'))
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,
                                 help_text=_('select file'))


class UploadNotesForm(forms.Form):
    file = forms.FileField()
