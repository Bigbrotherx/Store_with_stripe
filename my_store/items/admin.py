from django.contrib import admin

from .models import Item


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    '''Класс конфигурации модели Item в админке'''
    list_display = (
        'pk',
        'name',
        'price',
        'description',
        'currency',
        'image',
    )
    list_editable = ('currency',)
    search_fields = ('name',)
    list_filter = ('price',)
    empty_value_display = '-пусто-'
