from django.contrib import admin
from apps.task.models import *




class SaleTargetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'salesman', 'target_name', 'due_date', 'sales_target_revenue',
        'units_sold_target', 'avg_transaction_value_target', 'description',
        'target_period', 'progress', 'last_updated', 'date_added', 'creator'
    )
    search_fields = ('target_name', 'salesman__username', 'creator__username')  # Optional
    list_filter = ('due_date', 'salesman', 'creator')  # Optional

admin.site.register(SaleTarget, SaleTargetAdmin)

class SalesmanSalesTargetStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sales_target', 'status', 'completion_date', 'notes', 'last_updated','date_added', 'creator'
    )
    search_fields = ('sales_target__target_name', 'status')
    list_filter = ('status', 'sales_target')

admin.site.register(SalesmanSalesTargetStatus, SalesmanSalesTargetStatusAdmin)

class CustomerRelationshipTargetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'salesman', 'target_name', 'created_at', 'due_date', 'target_period',
        'customer_acquisition_target', 'customer_retention_target',
        'customer_satisfaction_score_target', 'loyalty_program_signups_target',
        'progress', 'description','creator','date_added'
    )
    search_fields = ('target_name', 'salesman__username', 'target_period')
    list_filter = ('due_date', 'salesman', 'target_period')

admin.site.register(CustomerRelationshipTarget, CustomerRelationshipTargetAdmin)

class SalesmanCustomerRelationshipTargetStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer_relationship_target', 'status', 'completion_date', 'notes', 'last_updated', 
    )
    search_fields = ('customer_relationship_target__target_name', 'status', 'notes')
    list_filter = ('status', 'customer_relationship_target')

admin.site.register(SalesmanCustomerRelationshipTargetStatus, SalesmanCustomerRelationshipTargetStatusAdmin)

class StaffTaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'staff', 'task_name', 'created_at', 'target_period', 'description',
        'due_date', 'priority', 'document', 'contact_file', 'image_1', 'image_2', 
        'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 
        'audio_1', 'audio_2', 'audio_3', 'audio_4', 'audio_5', 'audio_6', 'creator','date_added',
        'audio_7', 'audio_8'
    )
    search_fields = ('task_name', 'staff__username', 'description')
    list_filter = ('priority', 'due_date', 'created_at')

class SalesmanTaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'task', 'status', 'completion_date', 'notes', 'last_updated','creator','date_added'
    )
    search_fields = ('task__task_name', 'status', 'notes')
    list_filter = ('status', 'completion_date')

admin.site.register(StaffTask, StaffTaskAdmin)
admin.site.register(SalesmanTaskStatus, SalesmanTaskStatusAdmin)

class CompanyNotesAdmin(admin.ModelAdmin):
    list_display = ('note_title', 'note', 'audio', 'image', 'tags')
    search_fields = ('note_title', 'note', 'tags')
    list_filter = ('tags',)

class DeliveryAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'heading', 
        'location_place_name', 
        'delivery_area', 
        'delivery_date', 
        'delivery_type', 
        'status', 
        'amount',
        'customer_name', 
        'customer_address', 
        'customer_phone', 
        'pending_amount', 
        'payment_mode', 
        'note', 
        'call_report_followup', 
        'delivery_google_map_url',
        'delivered_staff', 
        'creator', 
        'date_added', 
        'is_deleted'
    ]

admin.site.register(Delivery, DeliveryAdmin)

class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ('task', 'previous_staff', 'new_staff', 'forwarded_at')
    search_fields = ('task__task_name', 'previous_staff__full_name', 'new_staff__full_name')
    list_filter = ('forwarded_at',)
    date_hierarchy = 'forwarded_at'

# Register the models with their respective admin classes
admin.site.register(CompanyNotes, CompanyNotesAdmin)
admin.site.register(DeliveryArea, DeliveryAreaAdmin)
admin.site.register(TaskHistory, TaskHistoryAdmin)
