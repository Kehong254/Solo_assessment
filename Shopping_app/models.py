from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone



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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart_id}, {self.user.username}"

    @property
    def total_price(self):
        return sum(item.item_price for item in self.cart_items.all())

    def add_item(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, volcano=volcano)
        cart_item.quantity += quantity
        cart_item.save()

    def remove_item(self, cart_item):
        cart_item.delete()

    def clear(self):
        self.cart_items.all().delete()

    def get_item_count(self):
        return self.cart_items.count()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    volcano = models.ForeignKey(Volcano, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cart.cart_id}, {self.quantity} x {self.volcano.Volcano_Name}"

    @property
    def item_price(self):
        return self.volcano.price * self.quantity

    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()

class Address(models.Model):
    Address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s address ({self.Address_id})"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    total_cost = models.FloatField()
    order_items = models.ManyToManyField(Volcano, through='OrderItem')

    def __str__(self):
        return f"Order {self.order_id} by {self.user_name}, total cost: ${self.total_cost}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    volcano = models.ForeignKey(Volcano, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.volcano.Volcano_Name} (Order {self.order.order_id})"
