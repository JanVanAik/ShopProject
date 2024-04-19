from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products_image', blank=True, null=True)
    desc = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'