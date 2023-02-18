from django.urls import path

from .views import index, product_detail

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('items/<int:id>/', product_detail, name='detail')
]
