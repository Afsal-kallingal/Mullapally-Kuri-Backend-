from django.utils import timezone
from rest_framework import serializers
from apps.task.models import SaleTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus , CompanyNotes ,TaskHistory
from apps.user_account.models import User
# from apps.task.models import SaleTarget
# from apps.main.functions import get_auto_id
from apps.main.serializers import BaseModelSerializer

class SaleTargetSerializer(BaseModelSerializer):
    class Meta:
        model = SaleTarget
        fields = '__all__'

class SalesmanSalesTargetStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanSalesTargetStatus
        fields = '__all__'

    #     fields = [
    #         'id',
    #         'sales_target',  # This should match the related name
    #         'completion_date',
    #         'status',
    #         'notes',
    #         'last_updated'
    #     ]

    # def validate(self, data):
    #     # Add validation logic if needed
    #     return data

    # def create(self, validated_data):
    #     return SalesmanSalesTargetStatus.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.completion_date = validated_data.get('completion_date', instance.completion_date)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.notes = validated_data.get('notes', instance.notes)
    #     instance.last_updated = timezone.now()
    #     instance.save()
    #     return instance

class CustomerRelationshipTargetSerializer(BaseModelSerializer):
    class Meta:
        model = CustomerRelationshipTarget
        fields = '__all__'

class SalesmanCustomerRelationshipTargetStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanCustomerRelationshipTargetStatus
        fields = '__all__'

class StaffTaskSerializer(BaseModelSerializer):
    class Meta:
        model = StaffTask
        fields = '__all__'

class SalesmanTaskStatusSerializer(BaseModelSerializer):
    class Meta:
        model = SalesmanTaskStatus
        fields = '__all__'

class ListViewStaffTaskSerializer(BaseModelSerializer):
    creator_name = serializers.CharField(source='creator.full_name',read_only=True)
    staff_name = serializers.CharField(source='staff.user.full_name',read_only=True)

    class Meta:
        model = StaffTask
        fields = ['id','staff','date_added','staff_name','task_name','creator_name','created_at','target_period','description','due_date','priority','audio','image','document','contact_file']

class ListViewResponseStaffTaskSerializer(BaseModelSerializer):
    task_name = serializers.CharField(source='task.task_name', read_only=True)
    task_description = serializers.CharField(source='task.description', read_only=True)
    task_starting_time = serializers.DateTimeField(source='task.created_at', read_only=True)
    task_creator = serializers.CharField(source='task.creator.full_name', read_only=True)
    task_duedate = serializers.DateTimeField(source='task.due_date', read_only=True)
    task_created_time = serializers.DateTimeField(source='task.date_added', read_only=True)
    assigned_staff= serializers.CharField(source='task.staff.user.full_name', read_only=True)

    class Meta:
        model = SalesmanTaskStatus
        fields = [
            'task','id', 'status', 'notes', 'completion_date', 'last_updated','assigned_staff',
            'task_name', 'task_description', 'task_starting_time', 'task_creator','task_duedate','task_created_time'
        ]

class ListViewResponseSalesTargetSerializer(BaseModelSerializer):
    sales_target_name = serializers.CharField(source='sales_target.target_name', read_only=True)
    sales_target_description = serializers.CharField(source='sales_target.description', read_only=True)
    sales_target_creator = serializers.CharField(source='sales_target.creator.full_name', read_only=True)
    sales_target_duedate = serializers.DateTimeField(source='sales_target.due_date', read_only=True)
    sales_target_created_time = serializers.DateTimeField(source='sales_target.date_added', read_only=True)
    assigned_staff = serializers.CharField(source='sales_target.salesman.full_name', read_only=True)  # or sales_target.staff.full_name based on your model
    sales_target_revenue = serializers.DecimalField(source='sales_target.sales_target_revenue', max_digits=10, decimal_places=2, read_only=True)
    units_sold_target = serializers.CharField(source='sales_target.units_sold_target', read_only=True)
    avg_transaction_value_target = serializers.DecimalField(source='sales_target.avg_transaction_value_target', max_digits=10, decimal_places=2, read_only=True)
    target_period = serializers.CharField(source='sales_target.target_period', read_only=True)
    progress = serializers.DecimalField(source='sales_target.progress', max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = SalesmanSalesTargetStatus
        fields = [
            'id',
            'sales_target',
            'completion_date',
            'status',
            'notes',
            'last_updated',
            'sales_target_name',
            'sales_target_description',
            'sales_target_creator',
            'sales_target_duedate',
            'sales_target_created_time',
            'assigned_staff',
            'sales_target_revenue',
            'units_sold_target',
            'avg_transaction_value_target',
            'target_period',
            'progress',
        ]

class ListViewCustomerRelationshipSerializer(BaseModelSerializer):
    customer_relationship_target_name = serializers.CharField(source='customer_relationship_target.target_name', read_only=True)
    customer_relationship_target_description = serializers.CharField(source='customer_relationship_target.description', read_only=True)
    customer_relationship_target_starting_time = serializers.DateTimeField(source='customer_relationship_target.created_at', read_only=True)
    customer_relationship_target_creator = serializers.CharField(source='customer_relationship_target.creator.full_name', read_only=True)
    customer_relationship_target_duedate = serializers.DateTimeField(source='customer_relationship_target.due_date', read_only=True)
    assigned_staff = serializers.CharField(source='customer_relationship_target.salesman.full_name', read_only=True)
    target_period = serializers.CharField(source='customer_relationship_target.target_period', read_only=True)
    customer_acquisition_target = serializers.IntegerField(source='customer_relationship_target.customer_acquisition_target', read_only=True)
    customer_retention_target = serializers.DecimalField(source='customer_relationship_target.customer_retention_target', max_digits=5, decimal_places=2, read_only=True)
    customer_satisfaction_score_target = serializers.DecimalField(source='customer_relationship_target.customer_satisfaction_score_target', max_digits=3, decimal_places=2, read_only=True)
    loyalty_program_signups_target = serializers.IntegerField(source='customer_relationship_target.loyalty_program_signups_target', read_only=True)
    progress = serializers.DecimalField(source='customer_relationship_target.progress', max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = SalesmanCustomerRelationshipTargetStatus
        fields = [
            'id',
            'customer_relationship_target',
            'completion_date',
            'status',
            'notes',
            'last_updated',
            'customer_relationship_target_name',
            'customer_relationship_target_description',
            'customer_relationship_target_starting_time',
            'customer_relationship_target_creator',
            'customer_relationship_target_duedate',
            'assigned_staff',
            'target_period',
            'customer_acquisition_target',
            'customer_retention_target',
            'customer_satisfaction_score_target',
            'loyalty_program_signups_target',
            'progress'
        ]

class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'

class CompanyNotesSerializer(BaseModelSerializer):
    class Meta:
        model = CompanyNotes
        fields = '__all__'


# class customer_relationship_targetBaseModelSerializer(serializers.ModelSerializer):
#     uuid = serializers.CharField(read_only=True)
#     auto_id = serializers.CharField(read_only=True)
#     creator = serializers.CharField(read_only=True)
#     date_added = serializers.CharField(read_only=True)

#     def create(self, validated_data):
#         validated_data["auto_id"] = get_auto_id(self.Meta.model)
#         validated_data["creator"] = self.context["request"].user
#         return super().create(validated_data)

#     class Meta:
#         abstract = True

# class SalesTargetSerializer(BaseModelSerializer):
#     class Meta:
#         model = SaleTarget
#         fields = [
#             'id',
#             'salesman',
#             'target_name',
#             'due_date',
#             'sales_target_revenue',
#             'units_sold_target',
#             'avg_transaction_value_target',
#             'description',
#             'target_period',
#             'progress',
#             'last_updated'
#         ]

#     def validate(self, data):
#         # You can add validation logic here if needed
#         return data

#     def create(self, validated_data):
#         return SaleTarget.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.salesman = validated_data.get('salesman', instance.salesman)
#         instance.target_name = validated_data.get('target_name', instance.target_name)
#         instance.due_date = validated_data.get('due_date', instance.due_date)
#         instance.sales_target_revenue = validated_data.get('sales_target_revenue', instance.sales_target_revenue)
#         instance.units_sold_target = validated_data.get('units_sold_target', instance.units_sold_target)
#         instance.avg_transaction_value_target = validated_data.get('avg_transaction_value_target', instance.avg_transaction_value_target)
#         instance.description = validated_data.get('description', instance.description)
#         instance.target_period = validated_data.get('target_period', instance.target_period)
#         instance.progress = validated_data.get('progress', instance.progress)
#         instance.last_updated = timezone.now()
#         instance.save()
#         return instance

# class SalesmanSalesTargetStatusSerializer(BaseModelSerializer):
#     class Meta:
#         model = SalesmanSalesTargetStatus
#         fields = [
#             'id',
#             'sales_target',
#             'completion_date',
#             'status',
#             'notes',
#             'last_updated'
#         ]

#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return SalesmanSalesTargetStatus.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.sales_target = validated_data.get('sales_target', instance.sales_target)
#         instance.completion_date = validated_data.get('completion_date', instance.completion_date)
#         instance.status = validated_data.get('status', instance.status)
#         instance.notes = validated_data.get('notes', instance.notes)
#         instance.last_updated = timezone.now()
#         instance.save()
#         return instance
    
# class SalesTargetListViewSerializer(TaskBaseModelSerializer):
#     # salesman = serializers.CharField(source='sales_target.salesman.username')
#     target_name = serializers.CharField(source='sales_target.target_name')
#     created_at = serializers.DateTimeField(source='sales_target.created_at')
#     due_date = serializers.DateField(source='sales_target.due_date')
#     sales_target_revenue = serializers.DecimalField(source='sales_target.sales_target_revenue', max_digits=10, decimal_places=2)
#     units_sold_target = serializers.IntegerField(source='sales_target.units_sold_target')
#     avg_transaction_value_target = serializers.DecimalField(source='sales_target.avg_transaction_value_target', max_digits=10, decimal_places=2)
#     description = serializers.CharField(source='sales_target.description')
#     target_period = serializers.CharField(source='sales_target.target_period')
#     progress = serializers.DecimalField(source='sales_target.progress', max_digits=5, decimal_places=2)  # Specify max_digits and decimal_places
#     last_updated = serializers.DateTimeField(source='sales_target.last_updated')

#     class Meta:
#         model = SalesmanSalesTargetStatus
#         fields = [
#             'id',
#             'sales_target',
#             # 'salesman',
#             'target_name',
#             'created_at',
#             'due_date',
#             'sales_target_revenue',
#             'units_sold_target',
#             'avg_transaction_value_target',
#             'description',
#             'target_period',
#             'progress',
#             'last_updated',
#             'completion_date',
#             'status',
#             'notes'
#         ]
        
# class CustomerRelationshipTargetSerializer(TaskBaseModelSerializer):
#     class Meta:
#         model = CustomerRelationshipTarget
#         fields = [
#             'id',
#             'salesman',
#             'target_name',
#             'created_at',
#             'due_date',
#             'target_period',
#             'customer_acquisition_target',
#             'customer_retention_target',
#             'customer_satisfaction_score_target',
#             'loyalty_program_signups_target',
#             'progress',
#             'description'
#         ]

#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return CustomerRelationshipTarget.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.salesman = validated_data.get('salesman', instance.salesman)
#         instance.target_name = validated_data.get('target_name', instance.target_name)
#         instance.due_date = validated_data.get('due_date', instance.due_date)
#         instance.target_period = validated_data.get('target_period', instance.target_period)
#         instance.customer_acquisition_target = validated_data.get('customer_acquisition_target', instance.customer_acquisition_target)
#         instance.customer_retention_target = validated_data.get('customer_retention_target', instance.customer_retention_target)
#         instance.customer_satisfaction_score_target = validated_data.get('customer_satisfaction_score_target', instance.customer_satisfaction_score_target)
#         instance.loyalty_program_signups_target = validated_data.get('loyalty_program_signups_target', instance.loyalty_program_signups_target)
#         instance.progress = validated_data.get('progress', instance.progress)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

# class SalesmanCustomerRelationshipTargetStatusSerializer(TaskBaseModelSerializer):
#     class Meta:
#         model = SalesmanCustomerRelationshipTargetStatus
#         fields = [
#             'id',
#             'customer_relationship_target',
#             'completion_date',
#             'status',
#             'notes',
#             'last_updated'
#         ]

#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return SalesmanCustomerRelationshipTargetStatus.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.customer_relationship_target = validated_data.get('customer_relationship_target', instance.customer_relationship_target)
#         instance.completion_date = validated_data.get('completion_date', instance.completion_date)
#         instance.status = validated_data.get('status', instance.status)
#         instance.notes = validated_data.get('notes', instance.notes)
#         instance.last_updated = timezone.now()
#         instance.save()
#         return instance

# class StaffTaskSerializer(TaskBaseModelSerializer):
#     class Meta:
#         model = StaffTask
#         fields = [
#             'id',
#             'staff',
#             'task_name',
#             'created_at',
#             'target_period',
#             'description',
#             'due_date',
#             'priority',
#             # 'auto_id',
#         ]

#     def validate(self, data):
#         # Add any custom validation here
#         return data

# # Debug line
#     def create(self, validated_data):
#         print(validated_data)
#         try:
#             instance = StaffTask.objects.create(**validated_data)
#             return instance
#         except Exception as e:
#             raise serializers.ValidationError({"error": str(e)})

#     def update(self, instance, validated_data):
#         instance.staff = validated_data.get('staff', instance.staff)
#         instance.task_name = validated_data.get('task_name', instance.task_name)
#         instance.target_period = validated_data.get('target_period', instance.target_period)
#         instance.description = validated_data.get('description', instance.description)
#         instance.due_date = validated_data.get('due_date', instance.due_date)
#         instance.priority = validated_data.get('priority', instance.priority)
#         instance.save()
#         return instance

# class SalesmanTaskStatusSerializer(TaskBaseModelSerializer):
#     class Meta:
#         model = SalesmanTaskStatus
#         fields = [
#             'id',
#             'task',
#             'status',
#             'notes',
#             'completion_date',
#             'last_updated'
#         ]

#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return SalesmanTaskStatus.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.task = validated_data.get('task', instance.task)
#         instance.status = validated_data.get('status', instance.status)
#         instance.notes = validated_data.get('notes', instance.notes)
#         instance.completion_date = validated_data.get('completion_date', instance.completion_date)
#         instance.last_updated = timezone.now()
#         instance.save()
#         return instance
