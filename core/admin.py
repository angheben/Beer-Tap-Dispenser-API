from django.contrib import admin
from .models import Beer


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'cost_per_liter', 'flow_volume', 'type', 'image']


admin.site.register(Beer, BeerAdmin)
