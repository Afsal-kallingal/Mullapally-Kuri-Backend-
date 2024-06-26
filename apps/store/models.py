
from django.db import models
from apps.main.models import BaseModel
from apps.product.models import Product
# from apps.product.models import Product


# class Purchase(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     purchase_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer.username} purchase on {self.purchase_date}"

# class PurchaseItem(models.Model):
#     purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.product.name} - {self.quantity}"