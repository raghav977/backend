

from rest_framework import serializers
from .models import Sale, SaleItem
from product.models import Product

class SaleItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = SaleItem
        fields = [
            'product', 'quantity', 'expiry_date', 'total_amount',
            'mrp', 'discount_percentage', 'free_products', 'total_discount', 'net_amount'
        ]

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'customer_name', 'pan_no', 'address', 'phone_number', 'date', 'items']
        read_only_fields = ['id', 'date']
    
    def validate(self,data):
        
        items = data.get('items')
        print("This is item",items)
        for prod in items:
            print("_____________________--_______________")
            product_ = prod.get('product')
            product_quantity = product_.quantity
            print(f"This is product quantity of the product {product_.name}is {product_quantity}")
            quantity = prod.get('quantity')
            print("This is quantity ",prod.get('quantity'))
            if quantity > product_quantity:
                raise serializers.ValidationError({"error":f"Insufficient quantity for product- {product_.name}. Available quantity is {product_quantity} "})
        
        return data
        

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sale.objects.create(**validated_data)

        for item in items_data:
            quantity = item['quantity']
            
            mrp = item['mrp']
            discount_pct = item.get('discount_percentage') or 0
            free_products = item.get('free_products') or 0

            total_amount = quantity * mrp
            total_discount = (total_amount) * (discount_pct / 100)
            net_amount = total_amount - total_discount

            SaleItem.objects.create(
                sale=sale,
                total_amount=total_amount,
                total_discount=total_discount,
                net_amount=net_amount,
                **item
            )
            product= item.get('product')
            product.quantity = product.quantity-quantity
            product.save()
        return sale
