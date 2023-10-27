from django.contrib import admin

# Register your models here.

from .models import Customer, Service, Unit, Inventory

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Unit)
admin.site.register(Inventory)