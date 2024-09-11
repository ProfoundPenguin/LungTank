from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('products', views.products, name='all_products'),
    path('legal', views.legal, name='legal'),
]