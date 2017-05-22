from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)