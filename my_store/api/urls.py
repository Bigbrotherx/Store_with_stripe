from django.urls import path

from .views import ItemsView

app_name = 'api'

urlpatterns = [
    path('<int:id>/', ItemsView.as_view()),
]
