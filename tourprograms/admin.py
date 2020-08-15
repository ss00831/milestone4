from django.contrib import admin
from .models import Tourprogram, Category

# Register your models here.

class TourprogramAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'region',
        'maximum',
        'priceadult',
        'pricechild',
        'departure_date',
        'estimated_times',
        'rating',
        'meeting_place',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Tourprogram, TourprogramAdmin)
admin.site.register(Category, CategoryAdmin)