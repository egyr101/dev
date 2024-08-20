
from django.contrib import admin
from django.urls import path, re_path
from main import views

urlpatterns = [
    re_path(r'sneakers/products|boots/products|bags/products|perfumery/products|accessories/products|sunglasses/products', views.products),
    path('', views.index, name=''),
    path('sneakers',views.sneakers),
    path('boots',views.boots),
    path('bags',views.bags),
    path('perfumery',views.perfumery),
    path('accessories',views.accessories),
    path('sunglasses',views.sunglasses),
]
