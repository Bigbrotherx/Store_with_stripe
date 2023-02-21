from django.urls import path

from .views import index, order

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('order/', order, name='order'),
]
