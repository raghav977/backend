# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from product.models import Product  # adjust based on your model names
from category.models import Category
from sales.models import Sale

from product.serializers import ProductSerializer
from sales.serializers import SaleSerializer
# from .serializers import ProductSerializer, SaleSerializer

User = get_user_model()

class DashboardStatsAPIView(APIView):
    def get(self, request):
        total_users = User.objects.count()
        total_products = Product.objects.count()
        total_categories = Category.objects.count()
        total_sales = Sale.objects.count()

        # Low stock: products with quantity <= 5 (customize this)
        low_stock_threshold = 5
        low_stock_products = Product.objects.filter(quantity__lte=low_stock_threshold)
        low_stock_count = low_stock_products.count()
        low_stock_data = ProductSerializer(low_stock_products, many=True).data


        return Response({
            'total_users': total_users,
            'total_products': total_products,
            'total_categories': total_categories,
            'total_sales': total_sales,
            'low_stock_count': low_stock_count,
            'low_stock_products': low_stock_data,
        }, status=status.HTTP_200_OK)
