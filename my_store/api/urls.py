from django.urls import path

from .views import ItemsView, create_an_order

app_name = 'api'

urlpatterns = [
    path('<int:id>/', ItemsView.as_view()),
    path('order/', create_an_order),
]
