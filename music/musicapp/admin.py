from django.contrib import admin
from .models import MusicCategory,FavoriteSong

# Register your models here.
admin.site.register(MusicCategory)
admin.site.register(FavoriteSong)