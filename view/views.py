from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def product_detail(request, slug):
    return render(request, 'product_detail.html')

def products(request):
    return render(request, 'products.html')

def legal(request):
    return render(request, 'legal.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def page404(request, exception=None):
    return render(request, '404.html', {}, status=404)
