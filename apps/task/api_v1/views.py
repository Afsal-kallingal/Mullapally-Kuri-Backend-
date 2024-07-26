from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.main.viewsets import BaseModelViewSet
from apps.task.models import SaleTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus ,CompanyNotes
from apps.task.api_v1.serializers import ListViewCustomerRelationshipSerializer,ListViewResponseSalesTargetSerializer,ListViewResponseStaffTaskSerializer,SaleTargetSerializer,ListViewStaffTaskSerializer,SalesmanSalesTargetStatusSerializer, CustomerRelationshipTargetSerializer, SalesmanCustomerRelationshipTargetStatusSerializer, StaffTaskSerializer, SalesmanTaskStatusSerializer ,CompanyNotesSerializer
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsTargetAdmin
from rest_framework.filters import SearchFilter
from django.utils.dateparse import parse_date
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


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
        if user.is_admin or user.target_admin:
            return SaleTarget.objects.all()
        return SaleTarget.objects.filter(salesman=user)
 
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
        if user.is_admin or user.target_admin:
            # Admins and target_admin users can see all statuses
            return SalesmanSalesTargetStatus.objects.all()
        else:
            # Regular users can only see statuses related to their assigned targets
            return SalesmanSalesTargetStatus.objects.filter(sales_target__salesman=user)

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
        if user.is_admin or user.target_admin:
            return CustomerRelationshipTarget.objects.all()
        return CustomerRelationshipTarget.objects.filter(salesman=user)

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
        if user.is_admin or user.target_admin:
            # Admins and target_admin users can see all statuses
            return SalesmanCustomerRelationshipTargetStatus.objects.all()
        else:
            # Regular users can only see statuses related to their assigned targets
            return SalesmanCustomerRelationshipTargetStatus.objects.filter(customer_relationship_target__salesman=user)

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
            return queryset.filter(staff=user)
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
            return queryset.filter(task__staff=user)

        return queryset
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def creators_task_listview(request):
    user = request.user
    tasks = StaffTask.objects.filter(creator=user)
    serializer = ListViewStaffTaskSerializer(tasks, many=True)
    return Response(serializer.data)

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
    tasks = StaffTask.objects.filter(staff=user)
    serializer = ListViewStaffTaskSerializer(tasks, many=True)
    return Response(serializer.data)

class CompanyNotesViewset(BaseModelViewSet):
    queryset = CompanyNotes.objects.all()
    serializer_class = CompanyNotesSerializer
    permission_classes = [IsAuthenticated]



# class SalesTargetViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = SalesTarget.objects.all()
#     serializer_class = SalesTargetSerializer

#     # filter_backends = [SearchFilter]
#     # search_fields = ['name','user__full_name']

#     # def get_queryset(self):
#     #     user = self.request.user
#     #     if user.is_admin or user.target_admin:
#     #         return SalesTarget.objects.all()
#     #     return SalesTarget.objects.filter(salesman=user)

#     def get_permissions(self):
#         if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
#             permission_classes = [IsAdmin | IsTargetAdmin]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]


#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Sales Target Deleted Successfully"}, status=status.HTTP_200_OK)

# class StaffSalesTargetStatusViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = SalesmanSalesTargetStatusSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.target_admin:
#             return SalesmanSalesTargetStatus.objects.all()
#         return SalesmanSalesTargetStatus.objects.filter(sales_target__salesman=user)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)

# class CustomerRelationshipTargetViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CustomerRelationshipTargetSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.target_admin:
#             return CustomerRelationshipTarget.objects.all()
#         return CustomerRelationshipTarget.objects.filter(salesman=user)

#     def get_permissions(self):
#         if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
#             permission_classes = [IsAdmin | IsTargetAdmin]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Customer Relationship Target Deleted Successfully"}, status=status.HTTP_200_OK)

# class StaffCustomerRelationshipstatusViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = SalesmanCustomerRelationshipTargetStatusSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.target_admin:
#             return SalesmanCustomerRelationshipTargetStatus.objects.all()
#         return SalesmanCustomerRelationshipTargetStatus.objects.filter(customer_relationship_target__salesman=user)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)

# class TaskViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = StaffTaskSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.target_admin:
#             return StaffTask.objects.all()
#         return StaffTask.objects.filter(staff=user)

#     def get_permissions(self):
#         if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
#             permission_classes = [IsAdmin | IsTargetAdmin]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Staff Task Deleted Successfully"}, status=status.HTTP_200_OK)

# class StaffTaskViewSet(BaseModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = SalesmanTaskStatusSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.target_admin:
#             return SalesmanTaskStatus.objects.all()
#         return SalesmanTaskStatus.objects.filter(task__staff=user)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Staff Task Deleted Successfully"}, status=status.HTTP_200_OK)
