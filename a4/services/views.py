from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderRequestForm

def services_brand(request):
    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Заполняем поле user текущим пользователем
            order.service = 'branding'  # Указываем услугу
            order.save()
            messages.success(request, 'Ваша заявка на брендинг успешно отправлена!')
            return redirect('services_brand')
        else:
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
    else:
        form = OrderRequestForm()

    return render(request, 'services/services-brand.html', {'form': form})

# Страница с Производством
def services_prod(request):
    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Заполняем поле user текущим пользователем
            order.service = 'production'  # Указываем услугу
            order.save()
            messages.success(request, 'Ваша заявка на производство успешно отправлена!')
            return redirect('services_prod')
        else:
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
    else:
        form = OrderRequestForm()

    return render(request, 'services/services-prod.html', {'form': form})

# Страница с Установкой
def services_install(request):
    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Заполняем поле user текущим пользователем
            order.service = 'installation'  # Указываем услугу
            order.save()
            messages.success(request, 'Ваша заявка на установку успешно отправлена!')
            return redirect('services_install')
        else:
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
    else:
        form = OrderRequestForm()

    return render(request, 'services/services-install.html', {'form': form})