# from django.shortcuts import render
# from rest_framework import viewsets


# # Create your views here.
# from sales.models import ProductSales
# from sales.serializers import ProductSalesSerializer

# class ProductSalesView(viewsets.ModelViewSet):
#     queryset = ProductSales.objects.all()
#     serializer_class = ProductSalesSerializer

# sales/views.py

from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.prefetch_related('items').all().order_by('-date')
    serializer_class = SaleSerializer
