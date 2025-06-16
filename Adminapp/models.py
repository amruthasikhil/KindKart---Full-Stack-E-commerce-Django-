from django.db import models



class CategoriesDb(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True) 
    description = models.TextField(blank=True)
    availability=models.CharField(max_length=50,default="Available")

class SubcategoriesDb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    categories=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    availability=models.CharField(max_length=50,default="Available")

class ProductDb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    subcategories=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    availability=models.CharField(max_length=50,default="Available")
    condition=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to="Product_images",null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)

class MembersDb(models.Model):
    pic = models.ImageField(upload_to='Members', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)







# Create your models here.
