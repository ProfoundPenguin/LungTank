import json
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Product

def get_cart(request):
    cart = request.COOKIES.get('cart', '{}')
    return json.loads(cart)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = get_cart(request)

    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {'name': product.name, 'price': str(product.price), 'quantity': 1}

    response = redirect('cart')  # Redirect to cart page
    response.set_cookie('cart', json.dumps(cart))
    return response

def remove_from_cart(request, product_id):
    cart = get_cart(request)
    if str(product_id) in cart:
        del cart[str(product_id)]

    response = redirect('cart')
    response.set_cookie('cart', json.dumps(cart))
    return response

def view_cart(request):
    cart = get_cart(request)
    return JsonResponse(cart)
