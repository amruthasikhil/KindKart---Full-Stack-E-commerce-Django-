from django.db import models


class UserDb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    mob=models.CharField(max_length=50,null=True,blank=True)
    pic=models.ImageField(upload_to="user_images",max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)

class CartDb(models.Model):
     userid=models.CharField(max_length=50,default=True,null=True)
     productid=models.CharField(max_length=50,default=True,null=True)
     totalprice=models.IntegerField(null=True,default=True)
     pimg=models.ImageField(upload_to="Cart_image",null=True,blank=True)

class ContactDb(models.Model):
     name=models.CharField(max_length=100,null=True,blank=True)
     phoneno=models.CharField(max_length=100,null=True,blank=True)
     email=models.EmailField(max_length=100,null=True,blank=True)
     subject=models.CharField(max_length=100,null=True,blank=True)
     message=models.CharField(max_length=100,null=True,blank=True)

class UserAddressDb(models.Model):
     userid=models.CharField(max_length=100,null=True,blank=True)
     place=models.CharField(max_length=100,null=True,blank=True)
     address=models.EmailField(max_length=100,null=True,blank=True)
     pincode=models.CharField(max_length=100,null=True,blank=True)

class OrderDb(models.Model):
     userid = models. CharField(max_length=100, null=True, blank=True)
     email = models. EmailField(max_length=100, null=True, blank=True)
     place = models. CharField(max_length=100, null=True, blank=True)
     address = models. CharField(max_length=100, null=True, blank=True)
     mobile = models. IntegerField(null=True, blank=True)
     pin = models. IntegerField(null=True, blank=True)
     totalPrice = models. IntegerField(null=True, blank=True)
     message = models. CharField(max_length=100, null=True, blank=True)
# Create your models here.
