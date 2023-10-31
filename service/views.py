from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Service, Unit, Inventory, CustomerForm, ServiceForm, UnitForm, InventoryForm
from address.models import Address

# Create your views here.

# Homepage
def index(request):
    return render(request, "service/index.html")

# List of Customers
def customers(request):
    customers = Customer.objects.all()
    return render(request, "service/customers.html", {
        "customers": customers
    })

# Displays specific unit and service history
def unit(request, unit_id):

    form = ServiceForm()    
    
    unit = Unit.objects.get(id=unit_id)

    if request.method == "POST":
        
        service = ServiceForm(request.POST)

        if service.is_valid():
            pass

            service.save()

    return render(request, "service/unit.html", {
        "unit": unit,
        "form":form
    })

# Shows Customer with units
def profile(request, profile_id):

    profile_id = Customer.objects.get(id=profile_id)

    units = Unit.objects.filter(customer=profile_id)

    return render(request, "service/profile.html", {
        "profile_id": profile_id,
        "units": units
    })

# Form for adding new Customer
def add_customer(request):
    
    if request.method == "POST":
        
        new_customer = CustomerForm(request.POST)

        if new_customer.is_valid():

            new_customer.save()

            return HttpResponseRedirect(reverse("customers"))

    form = CustomerForm()
    return render(request, "service/add_customer.html", {
        "form": form
    })

# Form for adding a new Unit
def add_unit(request):

    # adding a new Unit
    if request.method == "POST":

        new_unit = UnitForm(request.POST)

        if new_unit.is_valid():

            new_unit.save()

            return HttpResponseRedirect(reverse("customers"))

    form = UnitForm()
    return render(request, "service/add_unit.html", {
        "form": form
    })

def inventory(request):

    inventory = Inventory.objects.all()

    return render(request, "service/inventory.html", {
        "inventory": inventory
    })
