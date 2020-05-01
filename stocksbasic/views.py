from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Stock

def home(request):
  stocks = Stock.objects.all()
  return render(request, 'home.html', {'stocks': stocks})

def stock_details(request, id):
  try:
    stock = Stock.objects.get(id=id)
  except Stock.DoesNotExist:
    raise Http404('Stock Not Found!')
  return render(request, 'stock_details.html', {'stock': stock})