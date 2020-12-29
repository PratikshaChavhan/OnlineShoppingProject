from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    Cname=models.CharField(max_length=30)
    Cdiscription=models.CharField(max_length=300)

    def __str__(s):
        return s.Cname

class Product(models.Model):
    Pname=models.CharField(max_length=30)
    Price=models.IntegerField()
    Description=models.TextField(max_length=300)
    pimage=models.ImageField(upload_to='media/', default="")
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)


class Cart(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)        

class Order(models.Model):
    totalBill=models.IntegerField()
    orderdate=models.DateField(auto_now=True)
    status=models.CharField(max_length=30,default="processing")
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)

class FeedBack(models.Model):

    Comment=models.TextField(max_length=300)
    User=models.ForeignKey(User,on_delete=models.CASCADE)    

class MyImage(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
    myimage=models.ImageField(upload_to='media/')
    