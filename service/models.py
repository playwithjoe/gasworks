from django.db import models
from django.forms import ModelForm
from address.models import AddressField

# Models

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    company = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} Number: {self.phone}"
    
# Unit model for information on installed systems at Customer address
class Unit(models.Model):
    brand = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    address = AddressField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    # type, make (LG, Fijitsu, etc.), model (alphanumeric), serial number (unique identifier)

    def __str__(self):
        return f"{self.brand} owned by {self.customer}"

# Service to store info on installation, repair and service of Units
class Service(models.Model):
    date = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"Serviced unit {self.unit} on {self.date}"

# Inventory for parts and consumables
class Inventory(models.Model):
    name = models.CharField(max_length = 50)
    item_number = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=5, decimal_places=0)

# Forms listed below
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"