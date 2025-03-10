from django.shortcuts import render


def index(request):
    return render(request, 'reviews/reviews.html') # Страница с отзывами