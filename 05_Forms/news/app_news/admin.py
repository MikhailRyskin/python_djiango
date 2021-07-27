from django.contrib import admin
from .models import New, Comment
# Register your models here.


@admin.register(New, Comment)
class NewsAdmin(admin.ModelAdmin):
    pass
