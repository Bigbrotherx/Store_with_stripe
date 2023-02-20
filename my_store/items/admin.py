from django.contrib import admin

from .models import Item, Discount, Order


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    """Класс конфигурации модели Item в админке"""
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


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Класс конфигурации модели Discount в админке"""
    list_display = (
        'pk',
        'code',
        'discount_name',
        'percent_off',
        'duration',
    )
    list_editable = ('duration',)
    search_fields = ('discount_name',)
    list_filter = ('percent_off',)
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс конфигурации модели Order в админке"""
    list_display = (
        'pk',
        'discount',
        'created_at',
    )
    empty_value_display = '-пусто-'
