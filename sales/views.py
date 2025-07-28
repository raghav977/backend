# # from django.shortcuts import render
# # from rest_framework import viewsets


# # # Create your views here.
# # from sales.models import ProductSales
# # from sales.serializers import ProductSalesSerializer

# # class ProductSalesView(viewsets.ModelViewSet):
# #     queryset = ProductSales.objects.all()
# #     serializer_class = ProductSalesSerializer

# # sales/views.py

# from rest_framework import viewsets
# from .models import Sale,SaleItem
# from .serializers import SaleSerializer,SaleOutputSerializer

# class SaleViewSet(viewsets.ModelViewSet):
#     queryset = Sale.objects.prefetch_related('items').all()
#     serializer_class = SaleSerializer

# class SaleOutputView(viewsets.ModelViewSet):
#     queryset = Sale.objects.prefetch_related('items').all()
#     serializer_class = SaleOutputSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Sale
from .serializers import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().prefetch_related('items__product')
    serializer_class = SaleSerializer
    # permission_classes = [Al]
