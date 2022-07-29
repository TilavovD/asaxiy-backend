from django.db import models
from helpers.models import BaseModel
from common.models import User
from product.models import Product
# Create your models here.

class Region(BaseModel):
    name = models.CharField(max_length=128)

class District(BaseModel):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

class Cart(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart")
    is_active = models.BooleanField(default=False)



class Order(BaseModel):
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    region = models.ForeignKey(Region, related_name="orders", on_delete=models.CASCADE)
    district = models.ForeignKey(District, related_name="orders", on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    


class OrderProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_product")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    choices = (
        ('active', 'active'),
        ('passive', 'passive')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ordered_products")
    status = models.CharField(choices=choices, max_length=128)
    