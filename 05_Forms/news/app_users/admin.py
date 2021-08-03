from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'verification')
    list_filter = ['verification']

    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(verification=True)
        verif_group = Group.objects.get(name='верифицированный')
        for profile_user in queryset:
            profile_user.user.groups.add(verif_group)

    def deactivate(self, request, queryset):
        queryset.update(verification=False)
        verif_group = Group.objects.get(name='верифицированный')
        for profile_user in queryset:
            profile_user.user.groups.remove(verif_group)

    activate.short_description = 'верифицировать пользователя'
    deactivate.short_description = 'отменить верификацию'


admin.site.register(Profile, ProfileAdmin)