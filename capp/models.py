from django.db import models
from django.contrib import messages
#from django_google_maps import fields as map_fields
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    user= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add= True, null=True)

    def __str__(self):
        return self.user

class category(models.Model):
    resname = models.CharField(max_length=200, null=True)
    image =models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.resname

class product(models.Model):
    dname = models.CharField(max_length=200, null=True)
   

    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True,default= 1)
    categories = models.ForeignKey(category, null=True, on_delete=models.SET_NULL)
    amount=models.FloatField(null=True)

    def __str__(self):
        return self.dname
    

    

class order(models.Model):
    categories = models.ForeignKey(category, null=True, on_delete=models.SET_NULL)
    user= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    items= models.TextField(null=True)
    total = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   

class cart(models.Model):
    
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL, blank=True)
    total = models.FloatField(null=True)
    user= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)


   