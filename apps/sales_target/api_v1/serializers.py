from apps.main.serializers import BaseModelSerializer
from django.utils import timezone
from rest_framework import serializers
from apps.sales_target.models import SalesTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus
from apps.user_account.models import User

class SalesTargetSerializer(BaseModelSerializer):
    class Meta:
        model = SalesTarget
        fields = [
            'id',
            'salesman',
            'target_name',
            'created_at',
            'due_date',
            'sales_target_revenue',
            'units_sold_target',
            'avg_transaction_value_target',
            'description',
            'target_period',
            'progress',
            'last_updated'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return SalesTarget.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.salesman = validated_data.get('salesman', instance.salesman)
        instance.target_name = validated_data.get('target_name', instance.target_name)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.sales_target_revenue = validated_data.get('sales_target_revenue', instance.sales_target_revenue)
        instance.units_sold_target = validated_data.get('units_sold_target', instance.units_sold_target)
        instance.avg_transaction_value_target = validated_data.get('avg_transaction_value_target', instance.avg_transaction_value_target)
        instance.description = validated_data.get('description', instance.description)
        instance.target_period = validated_data.get('target_period', instance.target_period)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.last_updated = timezone.now()
        instance.save()
        return instance

class SalesmanSalesTargetStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanSalesTargetStatus
        fields = [
            'id',
            'sales_target',
            'completion_date',
            'status',
            'notes',
            'last_updated'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return SalesmanSalesTargetStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sales_target = validated_data.get('sales_target', instance.sales_target)
        instance.completion_date = validated_data.get('completion_date', instance.completion_date)
        instance.status = validated_data.get('status', instance.status)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.last_updated = timezone.now()
        instance.save()
        return instance
    
class SalesTargetListViewSerializer(BaseModelSerializer):
    # salesman = serializers.CharField(source='sales_target.salesman.username')
    target_name = serializers.CharField(source='sales_target.target_name')
    created_at = serializers.DateTimeField(source='sales_target.created_at')
    due_date = serializers.DateField(source='sales_target.due_date')
    sales_target_revenue = serializers.DecimalField(source='sales_target.sales_target_revenue', max_digits=10, decimal_places=2)
    units_sold_target = serializers.IntegerField(source='sales_target.units_sold_target')
    avg_transaction_value_target = serializers.DecimalField(source='sales_target.avg_transaction_value_target', max_digits=10, decimal_places=2)
    description = serializers.CharField(source='sales_target.description')
    target_period = serializers.CharField(source='sales_target.target_period')
    progress = serializers.DecimalField(source='sales_target.progress', max_digits=5, decimal_places=2)  # Specify max_digits and decimal_places
    last_updated = serializers.DateTimeField(source='sales_target.last_updated')

    class Meta:
        model = SalesmanSalesTargetStatus
        fields = [
            'id',
            'sales_target',
            # 'salesman',
            'target_name',
            'created_at',
            'due_date',
            'sales_target_revenue',
            'units_sold_target',
            'avg_transaction_value_target',
            'description',
            'target_period',
            'progress',
            'last_updated',
            'completion_date',
            'status',
            'notes'
        ]
        
class CustomerRelationshipTargetSerializer(BaseModelSerializer):
    class Meta:
        model = CustomerRelationshipTarget
        fields = [
            'id',
            'salesman',
            'target_name',
            'created_at',
            'due_date',
            'target_period',
            'customer_acquisition_target',
            'customer_retention_target',
            'customer_satisfaction_score_target',
            'loyalty_program_signups_target',
            'progress',
            'description'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return CustomerRelationshipTarget.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.salesman = validated_data.get('salesman', instance.salesman)
        instance.target_name = validated_data.get('target_name', instance.target_name)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.target_period = validated_data.get('target_period', instance.target_period)
        instance.customer_acquisition_target = validated_data.get('customer_acquisition_target', instance.customer_acquisition_target)
        instance.customer_retention_target = validated_data.get('customer_retention_target', instance.customer_retention_target)
        instance.customer_satisfaction_score_target = validated_data.get('customer_satisfaction_score_target', instance.customer_satisfaction_score_target)
        instance.loyalty_program_signups_target = validated_data.get('loyalty_program_signups_target', instance.loyalty_program_signups_target)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class SalesmanCustomerRelationshipTargetStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanCustomerRelationshipTargetStatus
        fields = [
            'id',
            'customer_relationship_target',
            'completion_date',
            'status',
            'notes',
            'last_updated'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return SalesmanCustomerRelationshipTargetStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer_relationship_target = validated_data.get('customer_relationship_target', instance.customer_relationship_target)
        instance.completion_date = validated_data.get('completion_date', instance.completion_date)
        instance.status = validated_data.get('status', instance.status)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.last_updated = timezone.now()
        instance.save()
        return instance

class StaffTaskSerializer(BaseModelSerializer):
    class Meta:
        model = StaffTask
        fields = [
            'id',
            'staff',
            'task_name',
            'created_at',
            'target_period',
            'description',
            'due_date',
            'priority'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return StaffTask.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff = validated_data.get('staff', instance.staff)
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.target_period = validated_data.get('target_period', instance.target_period)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance

class SalesmanTaskStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanTaskStatus
        fields = [
            'id',
            'task',
            'status',
            'notes',
            'completion_date',
            'last_updated'
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        return SalesmanTaskStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.status = validated_data.get('status', instance.status)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.completion_date = validated_data.get('completion_date', instance.completion_date)
        instance.last_updated = timezone.now()
        instance.save()
        return instance
