from django.contrib import admin
from .models import info, customer,city,restaurants

admin.site.register(info)
admin.site.register(customer)
admin.site.register(city)
admin.site.register(restaurants)