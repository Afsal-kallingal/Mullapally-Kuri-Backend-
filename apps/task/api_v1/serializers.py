from django.utils import timezone
from rest_framework import serializers
from apps.task.models import SaleTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus , CompanyNotes ,TaskHistory,Delivery,DeliveryArea
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

# class StaffTaskAudioSerializer(BaseModelSerializer):
#     class Meta(BaseModelSerializer.Meta):
#         model = StaffTaskAudio
#         fields = '__all__'

# class StaffTaskImageSerializer(BaseModelSerializer):
#     class Meta(BaseModelSerializer.Meta):
#         model = StaffTaskImage
#         fields = '__all__'

# class StaffTaskAudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffTaskAudio
#         fields = ['audio', 'task']

# class StaffTaskAudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffTaskAudio
#         fields = '__all__'

# class StaffTaskImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffTaskImage
#         fields = '__all__'

class StaffTaskSerializer(BaseModelSerializer):

    class Meta:
        model = StaffTask
        fields = '__all__'

        
class ListViewStaffTaskSerializer(BaseModelSerializer):
    creator_name = serializers.CharField(source='creator.full_name', read_only=True)
    staff_name = serializers.CharField(source='staff.user.full_name', read_only=True)
    image_1 = serializers.ImageField(read_only=True)
    image_2 = serializers.ImageField(read_only=True)
    image_3 = serializers.ImageField(read_only=True)
    image_4 = serializers.ImageField(read_only=True)
    image_5 = serializers.ImageField(read_only=True)
    image_6 = serializers.ImageField(read_only=True)
    image_7 = serializers.ImageField(read_only=True)
    image_8 = serializers.ImageField(read_only=True)
    audio_1 = serializers.FileField(read_only=True)
    audio_2 = serializers.FileField(read_only=True)
    audio_3 = serializers.FileField(read_only=True)
    audio_4 = serializers.FileField(read_only=True)
    audio_5 = serializers.FileField(read_only=True)
    audio_6 = serializers.FileField(read_only=True)
    audio_7 = serializers.FileField(read_only=True)
    audio_8 = serializers.FileField(read_only=True)

    class Meta:
        model = StaffTask
        fields = [
            'id', 'staff', 'date_added', 'staff_name', 'task_name', 'creator_name',
            'created_at', 'target_period', 'description', 'due_date', 'priority', 
            'document', 'contact_file',
            'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6',
            'image_7', 'image_8', 'audio_1', 'audio_2', 'audio_3', 'audio_4', 
            'audio_5', 'audio_6', 'audio_7', 'audio_8'
        ]

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

class DeliveryAreaSerializer(BaseModelSerializer):
    class Meta:
        model = DeliveryArea
        fields = '__all__'


class DeliverySerializer(BaseModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        # read_only_fields = ('delivered_staff')

