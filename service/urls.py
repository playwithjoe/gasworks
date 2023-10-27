from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers", views.customers, name="customers"),
    path("customers/<int:profile_id>", views.profile, name="profile"),
    path("customers/unit/<int:unit_id>", views.unit, name="unit"),
    path("add_customer", views.add_customer, name="add_customer"),
    path("add_unit", views.add_unit, name="add_unit"),
    path("inventory", views.inventory, name="inventory"),
]