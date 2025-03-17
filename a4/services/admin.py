from django.contrib import admin
from services.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'service',
        'price',
        'status',
        'completion_date',
        'is_completed'
    )
    list_filter = ('status', 'is_completed')
    search_fields = ('user__username', 'service')
    readonly_fields = ('user', 'service', 'created_at',)