from django.contrib import admin
from .models import customer,city,restaurants
# Register your models here.

admin.site.register(customer)
admin.site.register(city)
admin.site.register(restaurants)