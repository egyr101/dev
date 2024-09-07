
from django.contrib import admin
from django.urls import path, re_path
from main import views
from django.conf import settings
from django.conf.urls.static import static
from main.models import ProductCategory,Product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name=''),
    path('Кроссовки',views.sneakers),
    path('Ботинки',views.boots),
    path('Сумки',views.bags),
    path('Парфюмерия',views.perfumery),
    path('Аксессуары',views.accessories),
    path('Солнечныеочки',views.sunglasses),
    path('categories/<str:category>/names/<str:name>',views.product)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
