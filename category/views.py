from django.shortcuts import render

# Create your views here.
from category.serializers import CategorySerialzier
from rest_framework import viewsets
from category.models import Category
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    