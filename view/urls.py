from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('products', views.products, name='all_products'),
    path('legal', views.legal, name='legal'),
    path('faq', views.faq, name='faq'),
    path('tutorial', views.tutorial, name='tutorial'),
    path('safety', views.safety, name='safety'),
     path('contact', views.contact, name='contact'),
    path('refundPolicy', views.refund_policy, name='refund_policy'),
]
