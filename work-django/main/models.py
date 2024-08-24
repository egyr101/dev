from django.db import models

class NameProduct(models.Manager):
    def name_product(self,a):
        return self.filter(id=a)
class ProductCategory(models.Model):
    name = models.CharField(max_length = 128,unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to = 'product_images',default='images.jfif')
    category = models.ForeignKey(to=ProductCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

class Page(models.Model):
    page_direction = 0
    check_quality = True
