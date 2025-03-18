from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm
from services.models import Order


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)