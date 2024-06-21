from apps.main.serializers import BaseModelSerializer
from django.db import transaction
from apps.target.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User

class CustomerSerializer(BaseModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'auto_id', 'first_name', 'last_name', 'email', 'phone', 'billing_address',
            'shipping_address', 'customer_type', 'tax_id', 'notes', 'is_active', 
        ]
        # read_only_fields = ('auto_id', 'customer_id')  # Make auto_id and customer_id read-only to prevent manual setting

    # def create(self, validated_data):
    #     # Ensure atomicity
    #     with transaction.atomic():
    #         # Fetch the highest current customer_id
    #         last_customer = Customer.objects.all().order_by('customer_id').last()
    #         if last_customer:
    #             # Convert customer_id to int before incrementing
    #             next_customer_id = int(last_customer.customer_id) + 1
    #         else:
    #             next_customer_id = 1  # If there are no customers, start with 1

    #         # Assign the next customer_id
    #         validated_data['customer_id'] = next_customer_id

    #         # Debugging log to check the customer_id
    #         print(f"Creating new customer with customer_id: {next_customer_id}")

    #         # Create the new customer instance
    #         customer = Customer.objects.create(**validated_data)
        
    #     return customer

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
