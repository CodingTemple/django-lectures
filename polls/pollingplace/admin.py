from django.contrib import admin

#importing a module that is local to this file
from .models import Question

# Register your models here.
admin.site.register(Question)