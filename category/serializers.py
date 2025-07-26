from rest_framework import serializers
from category.models import Category

class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'
    pass