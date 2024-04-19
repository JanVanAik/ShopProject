from products.models import Product
from django.db import models
from users.models import User

# Create your models here.
class Basket(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина для {self.User.username}| Продукт {self.Product.name}"

    def sum(self):
        return self.quantity * self.Product.price

    def total_sum(self):
        baskets = Basket.objects.filter(User=self.User)
        total = 0
        for basket in baskets:
            total += basket.sum()
        return total

    def total_quantity(self):
        total = 0
        baskets = Basket.objects.filter(User=self.User)
        for basket in baskets:
            total += basket.quantity
        return total
