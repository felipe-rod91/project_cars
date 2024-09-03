from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'price')
    search_fields = ('model', 'brand')


admin.site.register(Car, CarAdmin)
