from apps.electrician.models import *
from apps.staff.models import *
from apps.task.models import *
from apps.client.models import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


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