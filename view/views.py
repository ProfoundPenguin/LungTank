from django.shortcuts import render
from django.http import HttpResponse
from product.models import *  # Import the Product model
from .models import *  # Import the Product model


def index(request):
    products = Product.objects.prefetch_related('images').all()  
    faqs = Faq.objects.all()
    data = {
        'products': products,
        'faqs': faqs,
    }

    return render(request, 'index.html', data) 

def product_detail(request, slug):
    return render(request, 'product_detail.html')

def faq(request):
    faqs = Faq.objects.all()
    data = {
        'faqs': faqs,
    }

    return render(request, 'faq.html', data) 

def products(request):
    products = Product.objects.prefetch_related('images').all()  
    data = {
        'products': products
    }
    return render(request, 'products.html', data)

def legal(request):
    return render(request, 'legal.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def page404(request, exception=None):
    return render(request, '404.html', {}, status=404)
