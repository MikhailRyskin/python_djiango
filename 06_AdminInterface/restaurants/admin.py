from django.contrib import admin
from .models import Restaurant, Waiter


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('основные сведения', {
            'fields': ('name', 'description', 'count_of_employers', 'director', 'chef')
        }),
        ('контакты', {
            'fields': ('phone', 'country', 'city', 'street', 'house')
        }),
        ('сервисы', {
            'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi',
                       'serves_burgers', 'serves_donats', 'serves_coffee')
        }),
    )


class WaiterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('ресторан', {
            'fields': ('restaurant',)
        }),
        ('основные сведения', {
            'fields': ('first_name', 'last_name', 'age', 'sex',)
        }),
        ('адрес', {
            'fields': ('country', 'city', 'street', 'house', 'apartment'),
            'classes': ['collapse']
        }),
        ('квалификация', {
            'fields': ('seniority', 'education', 'cources',),
            'description': 'образование, доп. курсы, опыт работы'
        }),
    )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
