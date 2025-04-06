from django.shortcuts import render


def packages(request):
    return render(request, 'packages/packages.html')