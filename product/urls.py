from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='cart'),
    path('decrement_from_cart/<int:product_id>/', decrement_from_cart, name='decrement_from_cart'),
]