from apps.electrician.models import *
from apps.staff.models import *
from apps.task.models import *
from apps.client.models import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Avg, Count


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_dashboard(request):
    # Count of tasks
    total_task_count = StaffTask.objects.count()
    
    # Task status counts
    pending_tasks_count = SalesmanTaskStatus.objects.filter(status='pending').count()
    in_progress_tasks_count = SalesmanTaskStatus.objects.filter(status='in_progress').count()
    completed_tasks_count = SalesmanTaskStatus.objects.filter(status='completed').count()
    
    # Prepare response data
    data = {
        'total_task_count': total_task_count,
        'pending_tasks_count': pending_tasks_count,
        'in_progress_tasks_count': in_progress_tasks_count,
        'completed_tasks_count': completed_tasks_count,
    }
    
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delivery_dashboard(request):
    total_deliveries = Delivery.objects.count()
    complete_deliveries = Delivery.objects.filter(status=Delivery.COMPLETE).count()
    pending_deliveries = Delivery.objects.filter(status=Delivery.PENDING).count()
    ongoing_deliveries = Delivery.objects.filter(status=Delivery.ONGOING).count()
    return_deliveries = Delivery.objects.filter(delivery_type=Delivery.RETURN).count()

    data = {
        'total_deliveries': total_deliveries,
        'completed_deliveries': complete_deliveries,
        'pending_deliveries': pending_deliveries,
        'ongoing_deliveries': ongoing_deliveries,
        'return_deliveries': return_deliveries
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_dashboard_report(request):
    total_clients = Client.objects.count()
    
    # Count of each client type
    end_user_count = Client.objects.filter(client_type='end_user').count()
    business_client_count = Client.objects.filter(client_type='business_client').count()
    government_count = Client.objects.filter(client_type='government').count()
    non_profit_count = Client.objects.filter(client_type='non_profit').count()
    
    data = {
        'total_clients': total_clients,
        'end_user_clients': end_user_count,
        'business_client_count': business_client_count,
        'government_client_count': government_count,
        'non_profit_client_count': non_profit_count,
    }
    
    return Response(data)

#sales target summery for the user -staff
@api_view(['GET'])
def staff_sales_target_summary(request):
    # Get the current user
    user = request.user
    
    # Retrieve the Staff instance for the current user
    staff = get_object_or_404(Staff, user=user)
    
    # Get all sale targets for the given staff member
    sale_targets = SaleTarget.objects.filter(salesman=staff)

    # Calculate the total sales target revenue
    total_sales_target_revenue = sale_targets.aggregate(total_revenue=Sum('sales_target_revenue'))['total_revenue'] or 0.00
    
    # Calculate the total progress
    total_sales_target_progress = sale_targets.aggregate(total_progress=Sum('progress'))['total_progress'] or 0.00

    # Prepare response data
    data = {
        'staff_id': staff.id,
        'total_sales_target_revenue': total_sales_target_revenue,
        'total_sales_target_progress': total_sales_target_progress,
    }

    return Response(data)

#Admin Dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sales_and_customer_relationship_dashboard(request):
    # Sales Target Aggregations
    total_sales_target_revenue = SaleTarget.objects.aggregate(total_revenue=Sum('sales_target_revenue'))['total_revenue'] or 0.00
    
    # Sales Target Progress
    total_sales_targets = SaleTarget.objects.count()
    total_sales_target_progress = SaleTarget.objects.aggregate(total_progress=Sum('progress'))['total_progress'] or 0.00
    # Sales Target Statuses
    pending_sales_targets_count = SalesmanSalesTargetStatus.objects.filter(status='pending').count()
    in_progress_sales_targets_count = SalesmanSalesTargetStatus.objects.filter(status='in_progress').count()
    completed_sales_targets_count = SalesmanSalesTargetStatus.objects.filter(status='completed').count()

    total_progress_sale_revenue = SalesmanSalesTargetStatus.objects.aggregate(total_progress_revenue=Sum('progress_sale_revenue'))['total_progress_revenue'] or 0.00

    # Customer Relationship Target Aggregations
    total_customer_acquisition_target = CustomerRelationshipTarget.objects.aggregate(total_acquisition=Sum('customer_acquisition_target'))['total_acquisition'] or 0
    total_customer_retention_target = CustomerRelationshipTarget.objects.aggregate(total_retention=Sum('customer_retention_target'))['total_retention'] or 0.00
    avg_customer_satisfaction_score_target = CustomerRelationshipTarget.objects.aggregate(avg_satisfaction=Avg('customer_satisfaction_score_target'))['avg_satisfaction'] or 0.00
    total_loyalty_program_signups_target = CustomerRelationshipTarget.objects.aggregate(total_signups=Sum('loyalty_program_signups_target'))['total_signups'] or 0
    
    # Customer Relationship Target Progress
    total_customer_relationship_targets = CustomerRelationshipTarget.objects.count()
    total_customer_relationship_target_progress = CustomerRelationshipTarget.objects.aggregate(total_progress=Sum('progress'))['total_progress'] or 0.00

    customer_relationship_target_pending_count = SalesmanCustomerRelationshipTargetStatus.objects.filter(status='pending').count()
    customer_relationship_target_completed_count = SalesmanCustomerRelationshipTargetStatus.objects.filter(status='completed').count()
    customer_relationship_target_in_progress_count = SalesmanCustomerRelationshipTargetStatus.objects.filter(status='in_progress').count()
    # Prepare the response data
    data = {
        'total_sales_target_revenue': total_sales_target_revenue,
        'total_sales_targets': total_sales_targets,
        'total_sales_target_progress': total_sales_target_progress,
        'pending_sales_targets_count': pending_sales_targets_count,
        'current_total_progress_sale_revenue' : total_progress_sale_revenue,
        'in_progress_sales_targets_count': in_progress_sales_targets_count,
        'completed_sales_targets_count': completed_sales_targets_count,
        'total_customer_acquisition_target': total_customer_acquisition_target,
        'total_customer_retention_target': total_customer_retention_target,
        'average_customer_satisfaction_score_target': avg_customer_satisfaction_score_target,
        'total_loyalty_program_signups_target': total_loyalty_program_signups_target,
        'total_customer_relationship_targets': total_customer_relationship_targets,
        'total_customer_relationship_target_progress': total_customer_relationship_target_progress,
        'customer_relationship_target_pending_count': customer_relationship_target_pending_count,
        'customer_relationship_target_completed_count': customer_relationship_target_completed_count,
        'customer_relationship_target_in_progress_count': customer_relationship_target_in_progress_count,
    }
    
    return Response(data)


#Staff View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def staff_customer_relationship_summary(request):
    # Get the current user
    user = request.user
    
    # Retrieve the Staff instance for the current user
    staff = get_object_or_404(Staff, user=user)
    
    # Get all customer relationship targets for the given staff member
    customer_relationship_targets = CustomerRelationshipTarget.objects.filter(salesman=staff)
    
    # Aggregate totals for CustomerRelationshipTarget
    total_customer_acquisition_target = customer_relationship_targets.aggregate(total_acquisition=Sum('customer_acquisition_target'))['total_acquisition'] or 0
    total_customer_retention_target = customer_relationship_targets.aggregate(total_retention=Sum('customer_retention_target'))['total_retention'] or 0.00
    avg_customer_satisfaction_score_target = customer_relationship_targets.aggregate(avg_satisfaction=Avg('customer_satisfaction_score_target'))['avg_satisfaction'] or 0.00
    total_loyalty_program_signups_target = customer_relationship_targets.aggregate(total_signups=Sum('loyalty_program_signups_target'))['total_signups'] or 0
    
    # Get all related SalesmanCustomerRelationshipTargetStatus instances
    relationship_target_status = SalesmanCustomerRelationshipTargetStatus.objects.filter(
        customer_relationship_target__salesman=staff
    )
    
    # Aggregate progress
    total_progress_customer_satisfaction_score = relationship_target_status.aggregate(
        total_progress=Sum('progress_customer_satisfaction_score')
    )['total_progress'] or 0.00

    # Prepare the response data
    data = {
        'total_customer_acquisition_target': total_customer_acquisition_target,
        'total_customer_retention_target': total_customer_retention_target,
        'average_customer_satisfaction_score_target': avg_customer_satisfaction_score_target,
        'total_loyalty_program_signups_target': total_loyalty_program_signups_target,
        'total_progress_customer_satisfaction_score': total_progress_customer_satisfaction_score,
    }
    
    return Response(data)

