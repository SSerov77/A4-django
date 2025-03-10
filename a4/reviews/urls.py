from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.index, name='reviews'),  # Страница с отзывами
]