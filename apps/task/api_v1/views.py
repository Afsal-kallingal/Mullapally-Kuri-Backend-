from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.main.viewsets import BaseModelViewSet
from apps.task.models import SaleTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus ,CompanyNotes ,TaskHistory,Delivery,DeliveryArea
from apps.task.api_v1.serializers import ListViewCustomerRelationshipSerializer,ListViewResponseSalesTargetSerializer,ListViewResponseStaffTaskSerializer,SaleTargetSerializer,ListViewStaffTaskSerializer,SalesmanSalesTargetStatusSerializer, CustomerRelationshipTargetSerializer, SalesmanCustomerRelationshipTargetStatusSerializer, StaffTaskSerializer, SalesmanTaskStatusSerializer ,CompanyNotesSerializer,TaskHistorySerializer,DeliverySerializer,DeliveryAreaSerializer
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsTargetAdmin
from rest_framework.filters import SearchFilter
from django.utils.dateparse import parse_date
from rest_framework.decorators import api_view, permission_classes
# from django_filters.rest_framework import DjangoFilterBackend
from apps.staff.models import Staff
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404

class SaleTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SaleTarget.objects.all()
    serializer_class = SaleTargetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['target_name','salesman__full_name','salesman__phone','salesman__username']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        queryset =  SaleTarget.objects.all()
        if not user.is_admin or user.target_admin:
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(salesman=staff)

        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(date_added=date)
            except ValueError:
                pass 
        return queryset
 
class SalesmanSalesTargetStatusViewSet(BaseModelViewSet):
    queryset = SalesmanSalesTargetStatus.objects.all()
    serializer_class = SalesmanSalesTargetStatusSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['sales_target__target_name','sales_target__salesman__full_name','sales_target__salesman__phone']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewResponseSalesTargetSerializer
        return SalesmanSalesTargetStatusSerializer

    def get_queryset(self):
        user = self.request.user
        queryset =  SalesmanSalesTargetStatus.objects.all()
        if not user.is_admin or user.target_admin:
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(sales_target__salesman=staff)

        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(date_added=date)
            except ValueError:
                pass 
        return queryset

class CustomerRelationshipTargetViewSet(BaseModelViewSet):
    queryset = CustomerRelationshipTarget.objects.all()
    serializer_class = CustomerRelationshipTargetSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        queryset =  CustomerRelationshipTarget.objects.all()
        if not user.is_admin or user.target_admin:
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(salesman=staff)

        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(date_added=date)
            except ValueError:
                pass 
        return queryset
    
class SalesmanCustomerRelationshipTargetStatusViewSet(BaseModelViewSet):
    queryset = SalesmanCustomerRelationshipTargetStatus.objects.all()
    serializer_class = SalesmanCustomerRelationshipTargetStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewCustomerRelationshipSerializer
        return SalesmanCustomerRelationshipTargetStatusSerializer

    def get_queryset(self):
        user = self.request.user
        queryset =  SalesmanCustomerRelationshipTargetStatus.objects.all()
        if not user.is_admin or user.target_admin:
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(customer_relationship_target__salesman=staff)

        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(date_added=date)
            except ValueError:
                pass 
        return queryset

class StaffTaskViewSet(BaseModelViewSet):
    queryset = StaffTask.objects.all()
    serializer_class = StaffTaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['staff__user__full_name', 'task_name', 'description'] 

    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
    #         permission_classes = [IsAdmin | IsTargetAdmin]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewStaffTaskSerializer
        return StaffTaskSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset =  StaffTask.objects.all()
        # if "date" in self.request.GET:
        #     queryset = queryset.filter(created_at=self.request.GET.get("date"))
        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(created_at__date=date)
            except ValueError:
                pass 
        if self.request.GET.get('start_date'):
            queryset = queryset.filter(date_added__gte=self.request.GET.get("start_date"))
        if self.request.GET.get('end_date'):
            queryset = queryset.filter(date_added__lte=self.request.GET.get("end_date"))
            
        if not user.is_admin or user.target_admin:
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(staff=staff)
            # queryset = queryset.filter(staff=user)
        return queryset
    
class SalesmanTaskStatusViewSet(BaseModelViewSet):
    queryset = SalesmanTaskStatus.objects.all()
    serializer_class = SalesmanTaskStatusSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['task__staff__full_name','task__task_name']


    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewResponseStaffTaskSerializer
        return SalesmanTaskStatusSerializer

    def get_queryset(self):
        user = self.request.user
        queryset =  SalesmanTaskStatus.objects.all()
        
        if "date" in self.request.GET:
            try:
                date_str = self.request.GET.get("date")
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(task__created_at__date=date)
            except ValueError:
                pass 
        if self.request.GET.get("complete") == "true":
            queryset = queryset.filter(status='completed')
        if self.request.GET.get("pending") == "true":
            queryset = queryset.filter(status='pending')
        if self.request.GET.get("in_progress") == "true":
            queryset = queryset.filter(status='in_progress')
        if self.request.GET.get('start_date'):
            queryset = queryset.filter(date_added__gte=self.request.GET.get("start_date"))
        if self.request.GET.get('end_date'):
            queryset = queryset.filter(date_added__lte=self.request.GET.get("end_date"))
        if not user.is_admin or user.target_admin:
            # Admins and target_admin users can see all statuses
            staff = get_object_or_404(Staff, user=user)
            queryset = queryset.filter(task__staff=staff)

        return queryset
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def creators_task_listview(request):
    user = request.user
    tasks = StaffTask.objects.filter(creator=user)
    serializer = ListViewStaffTaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def creator_task_delete_view(request, task_id):
    try:
        task = StaffTask.objects.get(id=task_id, creator=request.user)
    except StaffTask.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({"detail": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def creator_task_responce_view(request):
    user = request.user
    replys = SalesmanTaskStatus.objects.filter(task__creator=user)
    serializer = ListViewResponseStaffTaskSerializer(replys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_task(request):
    user = request.user
    staff = get_object_or_404(Staff, user=user)
    tasks = StaffTask.objects.filter(staff=staff)
    serializer = ListViewStaffTaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def forward_task(request, task_id):
    try:
        task = StaffTask.objects.get(pk=task_id)
    except StaffTask.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    new_staff_id = request.data.get('new_staff_id')

    if not new_staff_id:
        return Response({"error": "new_staff_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        new_staff = Staff.objects.get(pk=new_staff_id)
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)

    task.forward_task(new_staff)
    return Response({"status": "task forwarded"}, status=status.HTTP_200_OK)

class TaskHistoryViewSet(viewsets.ModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = TaskHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = TaskHistory.objects.all()
        task_id = self.request.query_params.get('task')
        if task_id:
            queryset = queryset.filter(task_id=task_id)
        return queryset

class CompanyNotesViewset(BaseModelViewSet):
    queryset = CompanyNotes.objects.all()
    serializer_class = CompanyNotesSerializer
    permission_classes = [IsAuthenticated]

class DeliveryAreaViewSet(BaseModelViewSet):
    queryset = DeliveryArea.objects.all()
    serializer_class = DeliveryAreaSerializer
    permission_classes = [IsAuthenticated]

class DeliveryViewSet(BaseModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]
