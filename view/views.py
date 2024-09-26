from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product  # Import the Product model

def index(request):
    products = Product.objects.prefetch_related('images').all()  
    data = {
        'products': products
    }

    return render(request, 'index.html', data) 

def product_detail(request, slug):
    return render(request, 'product_detail.html')

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
