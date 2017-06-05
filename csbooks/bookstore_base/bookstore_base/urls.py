"""bookstore_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from books.views import indexView,BookList,add_to_cart,cart,checkout,checkoutpost,braintreetoken,receipt
from userauth.views import user_login
urlpatterns = [
    url(r'^$',indexView.as_view(),name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^books/$',BookList.as_view(),name='Books'),
    url(r'^api-auth/', include('rest_framework.urls'),name='rest_framework_auth'),
    url(r'^api/v1/books/',include('books.urls'),name='Books_API_V1'),
    url(r'^userauth/',include('userauth.urls')),
    url(r'logout/$',include('userauth.urls'),name = 'logout'),
    url(r'^add/(?P<ISBN>[-\w]+)', add_to_cart, name='add_to_cart'),
    url(r'^checkout', checkout, name='checkout'),
    url(r'^postcheckout', checkoutpost, name='checkoutpost'),
    url(r'^braintreetoken/', braintreetoken, name='braintreetoken'),
    url(r'^receipt/', receipt, name='receipt'),
	#url(r'^remove/(?<ISBN>[-\w]+)', remove_from_cart, name="remove_from_cart"),
	url(r'^cart/', cart, name="cart"),
]
