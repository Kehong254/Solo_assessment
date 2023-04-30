from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Volcano(models.Model):
    Volcano_ID = models.IntegerField(primary_key=True, unique=True)
    Volcano_Name = models.CharField(max_length=100)
    Volcano_Image = models.URLField(max_length=100)
    Volcano_Type = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    epoch_period = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    quantity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(99)])

    def __str__(self):
        return f'{self.Volcano_Name} ({self.Volcano_Type}, {self.Country})'

    def get_latitude(self):
        return float(self.Latitude)

    def get_longitude(self):
        return float(self.Longitude)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    volcano = models.ForeignKey(Volcano, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=False, blank=False)  # Updated
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address