from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

def reviews(request):
    print("Запрос на страницу отзывов получен. Метод:", request.method)

    if request.method == 'POST':
        print("Обработка POST-запроса.")
        form = ReviewForm(request.POST)
        if form.is_valid():
            print("Форма валидна. Сохранение отзыва в базу данных.")
            form.save()
            messages.success(request, 'Спасибо за ваш отзыв!')
            print("Отзыв успешно сохранён. Перенаправление на страницу отзывов.")
            return redirect('reviews')
        else:
            print("Форма невалидна. Ошибки:", form.errors)
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
    else:
        print("Обработка GET-запроса. Отображение формы.")
        form = ReviewForm()

    # Получаем все отзывы из базы данных
    all_reviews = Review.objects.all().order_by('-created_at')
    print("Загружено отзывов из базы данных:", all_reviews.count())

    # Передаем форму и отзывы в шаблон
    return render(request, 'reviews/reviews.html', {
        'form': form,
        'reviews': all_reviews,
    })