# Generated by Django 5.1.7 on 2025-03-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('discussion', 'Обсуждение'), ('development', 'Проработка'), ('in_progress', 'В процессе'), ('review', 'Проверка'), ('awaiting_payment', 'Ожидание оплаты'), ('paid', 'Оплачено'), ('frozen', 'Заморожено'), ('cancelled', 'Отменено')], default='discussion', max_length=50, verbose_name='Статус'),
        ),
    ]
