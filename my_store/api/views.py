from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from items.models import Item, Discount, Order
from .utils import (
    create_product_id,
    get_price_id,
    create_session_id,
    get_create_coupons_id
)


class ItemsView(APIView):
    """View класс для получениия сессии оплаты 1 item"""
    def get(self, request, id, format=None):
        item = get_object_or_404(Item, id=id)
        create_product_id(item)
        strip_item = get_price_id(item)
        session_id = create_session_id([(strip_item, 1)])

        return Response({'session_id': session_id}, status=status.HTTP_200_OK)


@api_view(['PATCH', ])
def add_promo_to_order(request):
    """View функция для изменения Order"""
    if request.method == 'PATCH':
        promocode = request.data.get('promo_code')
        discount = Discount.objects.filter(code=promocode)
        order = Order.objects.all().last()
        if discount.exists():
            chosen_discount = discount.first()
            get_create_coupons_id(chosen_discount)
            order.discount = chosen_discount
            order.save(update_fields=['discount'])

            return Response(
                {'Message': 'Promocod was found'},
                status=status.HTTP_200_OK
            )
        else:
            order.discount = None
            order.save(update_fields=['discount'])
            return Response(
                {'Message': 'Promocod do not exists'},
                status=status.HTTP_404_NOT_FOUND
            )


@api_view(['POST', 'GET', ])
def create_an_order(request):
    """View функция для сохранения Order"""
    if request.method == 'POST':
        list_of_ids = request.data.get('order_items')
        order = Order()
        order.save()
        if len(list_of_ids):
            for id in list_of_ids:
                item = get_object_or_404(Item, id=id)
                order.items.add(item)

            return Response(
                {'Order creation status': 'Success'},
                status=status.HTTP_200_OK
            )

        return Response(
            {'Error_message': 'No items in order!'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'GET':
        """View функция получения сессии оплаты работает с последним заказом"""
        order = Order.objects.all().last()
        items = Item.objects.filter(order=order)
        discount_id = None
        if order.discount:
            discount_id = order.discount.discount_id
        list_of_items = []
        for item in items:
            create_product_id(item)
            strip_item = get_price_id(item)
            list_of_items.append((strip_item, 1))
        session_id = create_session_id(list_of_items, discount_id)

        return Response({'session_id': session_id}, status=status.HTTP_200_OK)
