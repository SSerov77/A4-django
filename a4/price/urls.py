from django.urls import path
from price import views

urlpatterns = [
    path('', views.index, name='price'),  # Страница с ценами
]