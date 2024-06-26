from apps.main.serializers import BaseModelSerializer
from django.db import transaction
from apps.target.models import *
from apps.product.models import Product
from apps.user_account.functions import validate_phone
from apps.user_account.models import User
from rest_framework import serializers

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

# class TargetSerializer(BaseModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

#     class Meta:
#         model = Target
#         fields = [
#             'id', 'name', 'description', 'start_datetime', 'end_datetime', 
#             'target_amount', 'achieved_amount', 'user', 'customer', 'products', 'status'
#         ]

#     def create(self, validated_data):
#         products_data = validated_data.pop('products')
#         target = Target.objects.create(**validated_data)
#         target.products.set(products_data)
#         return target

#     def update(self, instance, validated_data):
#         products_data = validated_data.pop('products', None)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.start_datetime = validated_data.get('start_datetime', instance.start_datetime)
#         instance.end_datetime = validated_data.get('end_datetime', instance.end_datetime)
#         instance.target_amount = validated_data.get('target_amount', instance.target_amount)
#         instance.achieved_amount = validated_data.get('achieved_amount', instance.achieved_amount)
#         instance.user = validated_data.get('user', instance.user)
#         instance.customer = validated_data.get('customer', instance.customer)
        
#         if products_data is not None:
#             instance.products.set(products_data)
#         instance.save()
#         return instance

class SalesTargetSerializer(BaseModelSerializer):
    class Meta:
        model = SalesTarget
        fields = [
            'id',
            'salesman',
            'period',
            'sales_target_revenue',
            'units_sold_target',
            'avg_transaction_value_target',
            'description',
            'status',
            'reply',
        ]

    def validate(self, data):
        """
        Custom validation logic if needed.
        """
        # Add custom validation if required
        return data

    def create(self, validated_data):
        """
        Create and return a new `SalesTarget` instance, given the validated data.
        """
        return SalesTarget.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `SalesTarget` instance, given the validated data.
        """
        instance.salesman = validated_data.get('salesman', instance.salesman)
        instance.period = validated_data.get('period', instance.period)
        instance.sales_target_revenue = validated_data.get('sales_target_revenue', instance.sales_target_revenue)
        instance.units_sold_target = validated_data.get('units_sold_target', instance.units_sold_target)
        instance.avg_transaction_value_target = validated_data.get('avg_transaction_value_target', instance.avg_transaction_value_target)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.reply = validated_data.get('reply', instance.reply)

        instance.save()
        return instance

class CustomerRelationshipTargetSerializer(BaseModelSerializer):
    class Meta:
        model = CustomerRelationshipTarget
        fields = [
            'id',
            'salesman',
            'period',
            'customer_acquisition_target',
            'customer_retention_target',
            'customer_satisfaction_score_target',
            'loyalty_program_signups_target',
            'description',
            'status',
            'reply',
        ]

    def validate(self, data):
        """
        Custom validation logic if needed.
        """
        # Add custom validation if required
        return data

    def create(self, validated_data):
        """
        Create and return a new `CustomerRelationshipTarget` instance, given the validated data.
        """
        return CustomerRelationshipTarget.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `CustomerRelationshipTarget` instance, given the validated data.
        """
        instance.salesman = validated_data.get('salesman', instance.salesman)
        instance.period = validated_data.get('period', instance.period)
        instance.customer_acquisition_target = validated_data.get('customer_acquisition_target', instance.customer_acquisition_target)
        instance.customer_retention_target = validated_data.get('customer_retention_target', instance.customer_retention_target)
        instance.customer_satisfaction_score_target = validated_data.get('customer_satisfaction_score_target', instance.customer_satisfaction_score_target)
        instance.loyalty_program_signups_target = validated_data.get('loyalty_program_signups_target', instance.loyalty_program_signups_target)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.reply = validated_data.get('reply', instance.reply)

        instance.save()
        return instance
    
class SalesmanSalesTargetUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = SalesTarget
        fields = ['id', 'status', 'reply']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.reply = validated_data.get('reply', instance.reply)
        instance.save()
        return instance

class SalesmanCustomerTargetUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = CustomerRelationshipTarget
        fields = ['id', 'status', 'reply']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.reply = validated_data.get('reply', instance.reply)
        instance.save()
        return instance
    
class DailyTaskSerializer(BaseModelSerializer):
    class Meta:
        model = StaffTask
        fields = [
            'id',
            'staff',
            'creator',
            'date_added',
            'task_name',
            'description',
            'due_date',
            'status',
            'priority'
        ]

    def update(self, instance, validated_data):
        instance.staff = validated_data.get('staff', instance.staff)
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance
    
# class ListViewDailyTaskSerializer(BaseModelSerializer):
#     class Meta:
#         model = StaffTask
#         fields = [
#             'id',
#             'creator',
#             'staff',
#             'task_name',
#             'description',
#             'due_date',
#             'status',
#             'priority'
#         ]