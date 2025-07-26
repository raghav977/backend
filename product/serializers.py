from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name',read_only=True)
    class Meta:
        model = Product
        fields =['id','name','category','quantity','category_name','actual_price','selling_price']
    