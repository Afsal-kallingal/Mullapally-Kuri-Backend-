from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.main.viewsets import BaseModelViewSet
from rest_framework.routers import DefaultRouter
from apps.sales_target.models import SalesTarget, SalesmanSalesTargetStatus, CustomerRelationshipTarget, SalesmanCustomerRelationshipTargetStatus, StaffTask, SalesmanTaskStatus
from apps.sales_target.api_v1.serializers import SalesTargetSerializer, SalesmanSalesTargetStatusSerializer, CustomerRelationshipTargetSerializer, SalesmanCustomerRelationshipTargetStatusSerializer, StaffTaskSerializer, SalesmanTaskStatusSerializer
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsTargetAdmin

class SalesTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesTargetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return SalesTarget.objects.all()
        return SalesTarget.objects.filter(salesman=user)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Sales Target Deleted Successfully"}, status=status.HTTP_200_OK)

class StaffSalesTargetStatusViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesmanSalesTargetStatusSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return SalesmanSalesTargetStatus.objects.all()
        return SalesmanSalesTargetStatus.objects.filter(sales_target__salesman=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)

class CustomerRelationshipTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerRelationshipTargetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return CustomerRelationshipTarget.objects.all()
        return CustomerRelationshipTarget.objects.filter(salesman=user)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Customer Relationship Target Deleted Successfully"}, status=status.HTTP_200_OK)

class StaffCustomerRelationshipstatusViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesmanCustomerRelationshipTargetStatusSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return SalesmanCustomerRelationshipTargetStatus.objects.all()
        return SalesmanCustomerRelationshipTargetStatus.objects.filter(customer_relationship_target__salesman=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_200_OK)

class TaskViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffTaskSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return StaffTask.objects.all()
        return StaffTask.objects.filter(staff=user)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Staff Task Deleted Successfully"}, status=status.HTTP_200_OK)

class StaffTaskViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesmanTaskStatusSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.target_admin:
            return SalesmanTaskStatus.objects.all()
        return SalesmanTaskStatus.objects.filter(task__staff=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Staff Task Deleted Successfully"}, status=status.HTTP_200_OK)
