from rest_framework import serializers
from product.models import Product

class DashboardSerializer(serializers.Serializer):
    total_products = ()
    total_sales = serializers.ModelSerializer()
    total_low_stock =serializers.ModelSerializer()
    recent_sales = serializers.ModelSerializer()