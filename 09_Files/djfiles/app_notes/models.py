from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField(blank=True, null=True)


class NoteImage(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/', null=True, blank=True)
