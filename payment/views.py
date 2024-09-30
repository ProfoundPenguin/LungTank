from django.shortcuts import render
import json

def get_cart(request):
    cart = request.COOKIES.get('cart', '{}')
    return json.loads(cart)

def checkout(request):
    cart = get_cart(request)  # Retrieve the cart
    cart_total = 0  # Initialize total price to zero

    # Calculate the total price by iterating through the cart
    for product_id, item in cart.items():
        price = float(item['price'])  # Convert the price to a float (if stored as a string)
        quantity = item['quantity']  # Get the quantity of the item
        cart_total += price * quantity  # Add to the total price

    # Prepare data for the template
    data = {
        'product_id': product_id,
        'cart': cart,
        'cart_total': "{:.2f}".format(cart_total),  # Format the total to 2 decimal places
    }

    return render(request, 'checkout.html', data)