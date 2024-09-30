import json
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Product, Product_Image
from django.shortcuts import get_object_or_404

def get_cart(request):
    cart = request.COOKIES.get('cart', '{}')
    return json.loads(cart)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)

    product_images = Product_Image.objects.filter(product=product).first()
    if product_images and product_images.original_image:
        image_url = product_images.original_image.url
    else:
        image_url = '' 

    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image': image_url  # Include the image URL
        }
    response = JsonResponse({'status': 'success', 'message': 'Item added to cart', 'cart': cart})
    response.set_cookie('cart', json.dumps(cart))
    return response

def decrement_from_cart(request, product_id):
    cart = get_cart(request)

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            # Optionally remove the item if quantity reaches 1
            del cart[str(product_id)]

        response = JsonResponse({'status': 'success', 'message': 'Item quantity decremented', 'cart': cart})
    else:
        response = JsonResponse({'status': 'error', 'message': 'Item not found in cart'}, status=404)

    response.set_cookie('cart', json.dumps(cart))
    return response

def remove_from_cart(request, product_id):
    cart = get_cart(request)

    if str(product_id) in cart:
        del cart[str(product_id)]
        response = JsonResponse({'status': 'success', 'message': 'Item removed from cart', 'cart': cart})
    else:
        response = JsonResponse({'status': 'error', 'message': 'Item not found in cart'}, status=404)

    response.set_cookie('cart', json.dumps(cart))
    return response

def view_cart(request):
    cart = get_cart(request)
    return JsonResponse({'cart': cart})