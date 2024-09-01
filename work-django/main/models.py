from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length = 128,unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField(upload_to = 'images')
    category = models.ForeignKey(to=ProductCategory,on_delete=models.CASCADE)
    gender = models.CharField(max_length=128)
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

class Page(models.Model):
    page_direction = 0
    url = 'http://127.0.0.1:8000'
    check_quality = True
    check_man = False
    check_woman = False
