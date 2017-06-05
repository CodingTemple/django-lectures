from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)

    def __str__(self):
        return self.first_name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

#class Car(models.Model):
   # name = models.CharField(max_length = 255)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    #photo = models.ImageField(upload_to='cars')