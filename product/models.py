from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    actual_price = models.DecimalField(default=0,max_digits=8,decimal_places=3)
    selling_price = models.DecimalField(default=0,max_digits=8,decimal_places=3)

    
    def __str__(self):
        return f"Product named: {self.name} belongs to {self.category.category_name}"
        