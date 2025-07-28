from django.db import models
from product.models import Product

class Sale(models.Model):
    customer_name = models.CharField(max_length=200)
    pan_no = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=140, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale to {self.customer_name} on {self.date.strftime('%Y-%m-%d')}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='sale_items')
    quantity = models.IntegerField(default=0)
    expiry_date = models.DateField()
    total_amount = models.DecimalField(default=0, max_digits=9, decimal_places=3)
    mrp = models.DecimalField(default=0, max_digits=9, decimal_places=3)
    discount_percentage = models.DecimalField(default=0, max_digits=9, decimal_places=3)  # remove blank/null for safer calculations
    free_products = models.IntegerField(default=0)  # remove blank/null for safety
    total_discount = models.DecimalField(default=0, max_digits=9, decimal_places=3)  # keep consistent scale and precision, remove blank/null
    net_amount = models.DecimalField(default=0, max_digits=9, decimal_places=3)  # same here

    def __str__(self):
        return f"{self.product.name if self.product else 'Unknown product'} - Qty: {self.quantity} for Sale ID: {self.sale.id}"
