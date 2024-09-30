from django.urls import path
from .views import *

urlpatterns = [
    path('checkout', checkout, name='add_to_cart'),
]