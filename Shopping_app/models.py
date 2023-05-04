from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


class Volcano(models.Model):
  Volcano_ID = models.IntegerField(primary_key=True, unique=True)
  Volcano_Name = models.CharField(max_length=100)
  Volcano_Image = models.URLField(max_length=100)
  Volcano_Type = models.CharField(max_length=100)
  Country = models.CharField(max_length=100)
  epoch_period = models.CharField(max_length=100)
  Latitude = models.CharField(max_length=50)
  Longitude = models.CharField(max_length=50)
  price = models.FloatField()
  quantity = models.PositiveIntegerField()

  def __str__(self):
      return f'{self.Volcano_ID}, {self.Volcano_Name}, {self.Volcano_Type}, {self.Country}, {self.Latitude}, {self.Longitude}'



class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.cart_id}, {self.name}, {self.quantity}, {self.price}'

    def total_price(self):
        return sum(item.quantity * item.volcano.price for item in self.cart_items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    volcano = models.ForeignKey(Volcano, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cart.cart_id}, {self.volcano.Volcano_Name}, {self.quantity}'

