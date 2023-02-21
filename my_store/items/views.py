from django.shortcuts import render
from django.db.models import Sum

from .models import Item, Order


def index(request):
    """View функция главной страницы с товарами."""
    template = 'items/index.html'
    items = Item.objects.all()
    context = {
        'items': items
    }

    return render(request, template, context)


def order(request):
    """View функция страницы заказа."""
    template = 'items/order.html'
    order = Order.objects.all().last()
    total = order.items.aggregate(Sum('price')).get('price__sum')
    context = {
        'order': order,
        'total_price': total,
    }

    return render(request, template, context)
