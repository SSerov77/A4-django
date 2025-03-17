from django.shortcuts import render, redirect
from django.contrib import messages
from services.forms import OrderForm


def services_brand(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_brand')
            else:
                messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.error(request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь.')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-brand.html', {'form': form})


def services_prod(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_prod')
            else:
                messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.error(request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь.')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-prod.html', {'form': form})


def services_install(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_install')
            else:
                messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.error(request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь.')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-install.html', {'form': form})