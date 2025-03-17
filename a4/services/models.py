from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('discussion', 'Обсуждение'),
        ('development', 'Проработка'),
        ('in_progress', 'В процессе'),
        ('review', 'Проверка'),
        ('awaiting_payment', 'Ожидание оплаты'),
        ('paid', 'Оплачено'),
        ('frozen', 'Заморожено'),
        ('cancelled', 'Отменено'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    service = models.CharField(max_length=255, verbose_name="Услуга")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Цена"
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='discussion',
        verbose_name="Статус"
    )
    completion_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата окончания"
    )
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return f"Заказ от пользователя {self.user.username} на {self.service}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"