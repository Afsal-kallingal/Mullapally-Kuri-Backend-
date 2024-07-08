from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.main.viewsets import BaseModelViewSet
from apps.task.models import SaleTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus
from apps.task.api_v1.serializers import SaleTargetSerializer, SalesmanSalesTargetStatusSerializer, CustomerRelationshipTargetSerializer, SalesmanCustomerRelationshipTargetStatusSerializer, StaffTaskSerializer, SalesmanTaskStatusSerializer
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsTargetAdmin

class SaleTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SaleTarget.objects.all()
    serializer_class = SaleTargetSerializer

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

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return StaffTask.objects.all()
        return StaffTask.objects.filter(staff=user)

class SalesmanTaskStatusViewSet(BaseModelViewSet):
    queryset = SalesmanTaskStatus.objects.all()
    serializer_class = SalesmanTaskStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            # Admins and target_admin users can see all statuses
            return SalesmanTaskStatus.objects.all()
        else:
            # Regular users can only see statuses related to their assigned targets
            return SalesmanTaskStatus.objects.filter(task__staff=user)

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
