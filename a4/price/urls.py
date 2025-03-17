from django.urls import path
from price import views


urlpatterns = [
    path('', views.price, name='price'),  # Страница с ценами
]