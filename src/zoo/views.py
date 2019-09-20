from django.shortcuts import render
from django.views.generic import ListView

from zoo.models import Continente

# Create your views here.

class ContinenteList(ListView):
	model= Continente
	template_name = 'list.html'