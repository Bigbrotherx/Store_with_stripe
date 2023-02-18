from django.shortcuts import render

from .models import Item


def index(request):
    """View функция главной страницы с товарами"""
    template = 'items/index.html'
    items = Item.objects.all()
    context = {
        'items': items
    }

    return render(request, template, context)


def product_detail(requset):
    pass
