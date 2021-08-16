from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    fields = ('user', 'text')
    list_display = ('user', 'text', 'created_date', 'publication_date')


admin.site.register(Note, NoteAdmin)
