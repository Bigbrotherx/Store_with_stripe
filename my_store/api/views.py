from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import ItemSerializer
from items.models import Item
from .utils import get_price_id, get_session_id


class ItemsView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, id, format=None):
        item = get_object_or_404(Item, id=id)
        strip_item = get_price_id(item)
        session_id = get_session_id(strip_item)
        return Response({'session_id': session_id}, status=status.HTTP_200_OK)
