from django.shortcuts import render
from django.views import generic
from .models import MusicCategory,FavoriteSong

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'song_list'

    def get_queryset(self):
        return FavoriteSong.objects.order_by('Song_Name')[:6]


class DetailView(generic.DetailView):
    template_name = 'music/detail.html'
    model = FavoriteSong

class NotebookView(generic.TemplateView):
    template_name = 'music/NotableDjangoErrors.html'
