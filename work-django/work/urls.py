
from django.contrib import admin
from django.urls import path, re_path
from main import views
from main.models import ProductCategory,Product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name=''),
    path('Кроссовки',views.sneakers),
    path('Ботинки',views.boots),
    path('Сумки',views.bags),
    path('Парфюмерия',views.perfumery),
    path('Аксессуары',views.accessories),
    path('Солнечные очки',views.sunglasses),
    path('categories/<str:category>/names/<str:name>',views.product)
]
