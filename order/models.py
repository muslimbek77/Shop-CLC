import datetime
from django.db import models
from helpers.models import BaseModel
from common.models import User
from product.models import Product
from django.utils.translation import gettext as _



class Card(BaseModel):
    costumer = models.ForeignKey(User, 
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)

class Order(BaseModel):
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    payment_type = models.CharField(max_length=200)
    # card = models.ForeignKey(Card, on_delete=models.CASCADE)


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)





