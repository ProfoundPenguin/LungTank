from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola cabrone")

def product_detail(request, slug):
    return HttpResponse("Product")

def products(request):
    return HttpResponse("Products")

def legal(request):
    return HttpResponse("Legal")
