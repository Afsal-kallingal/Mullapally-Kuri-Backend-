from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.target.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User

class CustomerSerializer(BaseModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone', 'billing_address',
            'shipping_address', 'customer_type', 'tax_id', 'notes', 'is_active', 'customer_id'
        ]

class TargetSerializer(BaseModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    # products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Target
        fields = [
            'id', 'name', 'description', 'start_datetime', 'end_datetime', 
            'target_amount', 'achieved_amount', 'user', 'customer', 'products'
        ]

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        target = Target.objects.create(**validated_data)
        target.products.set(products_data)
        return target

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products', None)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.start_datetime = validated_data.get('start_datetime', instance.start_datetime)
        instance.end_datetime = validated_data.get('end_datetime', instance.end_datetime)
        instance.target_amount = validated_data.get('target_amount', instance.target_amount)
        instance.achieved_amount = validated_data.get('achieved_amount', instance.achieved_amount)
        instance.user = validated_data.get('user', instance.user)
        instance.customer = validated_data.get('customer', instance.customer)
        
        if products_data is not None:
            instance.products.set(products_data)
            
        instance.save()
        return instance
