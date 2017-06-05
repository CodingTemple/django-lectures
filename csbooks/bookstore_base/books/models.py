from django.db import models
from isbn_field import ISBNField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    ISBN = ISBNField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2,max_digits=8)
    author = models.CharField(max_length=256)

class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100,null=True)
    payment_id = models.CharField(max_length=100,null=True)

    def add_to_cart(self,ISBN):
        product = Book.objects.get(pk=ISBN)
        try:
            preexisting_order = CartProduct.objects.get(product_id=ISBN,cart=self)
            preexisting_order.quantity +=1
            preexisting_order.save()
        except (CartProduct.DoesNotExist):
            new_order = CartProduct.objects.create(product_id = ISBN, cart = self, quantity = 1)
            new_order.save()
    def remove_from_cart(self,ISBN):
        product = Book.objects.get(pk=ISBN)
        try:
            preexisting_order = CartProduct.objects.get(product_id=ISBN,cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -=1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except(CartProduct.DoesNotExist):
            pass

class CartProduct(models.Model):
    product = models.ForeignKey(Book)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()
