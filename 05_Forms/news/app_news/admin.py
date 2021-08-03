from django.contrib import admin
from .models import New, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class NewAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'tag')
    list_display = ('title', 'created_at', 'updated_at', 'activity')
    list_filter = ['created_at', 'tag']
    inlines = [CommentInline]

    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(activity=True)

    def deactivate(self, request, queryset):
        queryset.update(activity=False)

    activate.short_description = 'перевести в статус Активна'
    deactivate.short_description = 'перевести в статус Неактивна'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('what_new', 'user_name', 'text')
    list_filter = ['user_name']

    actions = ['comment_deleted']

    def comment_deleted(self, request, queryset):
        queryset.update(text='Удалено администратором')

    comment_deleted.short_description = 'удалить текст комментария'


admin.site.register(New, NewAdmin)
admin.site.register(Comment, CommentAdmin)
