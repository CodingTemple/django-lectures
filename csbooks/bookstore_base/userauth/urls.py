from django.conf.urls import url
from . import views

#TEMPLATE URLS
app_name = 'userauth'
urlpatterns = [
    url(r'^register/$', views.register, name = 'register'),
    url(r'^user_login/$',views.user_login, name = 'user_login'),
]
