# Generated by Django 5.1.7 on 2025-04-09 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255, verbose_name='Услуга')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('status', models.CharField(choices=[('discussion', 'Обсуждение'), ('development', 'Проработка'), ('in_progress', 'В процессе'), ('review', 'Проверка'), ('awaiting_payment', 'Ожидание оплаты'), ('paid', 'Оплачено'), ('frozen', 'Заморожено'), ('cancelled', 'Отменено')], default='discussion', max_length=50, verbose_name='Статус')),
                ('completion_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
