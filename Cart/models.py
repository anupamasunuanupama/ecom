from django.db import models
from Product.models import ProductDetails
from django.contrib.auth.models import User

class Cart(models.Model):
    product =models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    numberofitems =models.IntegerField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
  
    status =models.BooleanField(default=False)
    
class PurchasedItems(models.Model):
    product =models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    paymentstaus =models.BooleanField(default=False)

# Create your models here.
