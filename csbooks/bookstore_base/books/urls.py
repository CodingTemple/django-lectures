from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ListCreateBook.as_view(),name='Book_API'),
]
