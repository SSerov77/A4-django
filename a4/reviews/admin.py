from django.contrib import admin
from reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    search_fields = ('author', 'created_at')
