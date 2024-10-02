from django.shortcuts import render
from django.http import HttpResponse
from product.models import *  # Import the Product model
from .models import *  # Import the Product model


def index(request):
    products = Product.objects.prefetch_related('images').all().order_by('sales_count')[:8]
    landing = Landing.load()
    video_file_url = landing.video.url 
    faqs = Faq.objects.all()
    reviews = Review.objects.all().order_by('-rating', '-created_at')[:3]

    data = {
        'products': products,
        'faqs': faqs,
        'landing_video': video_file_url,
        'reviews': reviews,
    }

    return render(request, 'index.html', data) 

def product_detail(request, slug):
    return render(request, 'product_detail.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def contact(request):
    return render(request, 'contact.html')

def safety(request):
    return render(request, 'safety.html')

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
