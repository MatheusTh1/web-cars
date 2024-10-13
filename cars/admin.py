from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brands", "factory_year", "model_year", "value")
    search_fields = ("model", "factory_year")

admin.site.register(Car, CarAdmin)