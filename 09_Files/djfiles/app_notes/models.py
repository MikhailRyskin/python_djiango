from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))
    publication_date = models.DateTimeField(blank=True, null=True, verbose_name=_('publication date'))

    class Meta:
        verbose_name_plural = _('notes')
        verbose_name = _('note')


class NoteImage(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/', null=True, blank=True)
