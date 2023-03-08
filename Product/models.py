from django.db import models
from django.contrib.auth.models import User

class ProductDetails(models.Model):
    Product_Id=models.AutoField(primary_key=True)
    Product_Name=models.CharField(max_length=255)
    Product_Brand=models.CharField(max_length=255)
    Product_Description=models.CharField(max_length=1000)
    Product_Price=models.IntegerField()
    Product_Category=models.CharField(max_length=255)
    Product_Stock=models.PositiveIntegerField()
    Product_Image=models.ImageField(upload_to="product_image")
    Merchant=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    
# Create your models here.
