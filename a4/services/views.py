from django.shortcuts import render


# Страница с Брендингом
def services_brand(request):
    return render(request, 'services/services-brand.html')

# Страница с Брендингом
def services_prod(request):
    return render(request, 'services/services-prod.html')

# Страница с Брендингом
def services_install(request):
    return render(request, 'services/services-install.html')