#Django Imports

from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from .models import Book,Cart,CartProduct
# REST FRAMEWORK IMPORTS
from rest_framework import generics
from .serializers import BookSerializer

import braintree
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse,JsonResponse
# Create your views here.
class BookList(ListView):
    template_name = 'books/book_list'
    model = Book


class ListCreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class indexView(TemplateView):
    template_name = 'books/index.html'

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                merchant_id="MERCHANT_ID",
                                public_key="PUBLIC_KEY",
                                private_key = "PRIVATE_KEY")

def checkout(request):
    return render(request,'books/checkout.html')
@csrf_exempt
def checkoutpost(request):
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce')
        result = braintree.Transaction.sale({
            "amount": "10.00",
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True
            }
        })
        return redirect('/receipt')
    else:
        return HttpResponse('500')

def braintreetoken(request):
    return JsonResponse(braintree.ClientToken.generate(), safe=False)

def receipt(request):
    return render(request, 'books/receipt.html')


def add_to_cart(request, ISBN):
    if request.user.is_authenticated():
        #return JsonResponse(ISBN, safe=False)
        try:
            product = Book.objects.get(pk=ISBN)

        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user = request.user
                )
                cart.save()

            cart.add_to_cart(ISBN)

        return redirect('/cart')
    else:
        return HttpResponse('403')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user.id, active=True)
        orders = CartProduct.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.product.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total':total,
            'count':count,
        }
        return render(request, 'books/cart.html', context)
    else:
        return redirect('index')
