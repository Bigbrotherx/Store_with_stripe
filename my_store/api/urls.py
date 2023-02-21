from django.urls import path

from .views import ItemsView, create_an_order, add_promo_to_order

app_name = 'api'

urlpatterns = [
    path('<int:id>/', ItemsView.as_view()),
    path('order/', create_an_order),
    path('order/promo', add_promo_to_order),
]
