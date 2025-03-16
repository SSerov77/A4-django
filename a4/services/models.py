from django.db import models
from django.contrib.auth.models import User

class OrderRequest(models.Model):
    SERVICE_CHOICES = [
        ('branding', 'Брендинг'),
        ('production', 'Производство'),
        ('installation', 'Установка'),
    ]

    SUB_SERVICE_CHOICES = [
        # Подуслуги для брендинга
        ('logo', 'Создание логотипа'),
        ('colors', 'Подбор цветовых палитр'),
        ('events', 'Брендирование мероприятий'),
        # Подуслуги для производства
        ('signs', 'Изготовление вывесок'),
        ('materials', 'Материалы для торговых точек'),
        ('navigation', 'Навигационные системы'),
        # Подуслуги для установки
        ('strategies', 'Создание рекламных стратегий'),
        ('consulting', 'Консультации по брендингу'),
        ('slogans', 'Разработка слоганов'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, verbose_name="Услуга")
    sub_service = models.CharField(max_length=50, choices=SUB_SERVICE_CHOICES, verbose_name="Подуслуга")
    description = models.TextField(verbose_name="Описание заказа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заявка от {self.user.username} на {self.get_service_display()}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"