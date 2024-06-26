from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.salary_finance.models import *
from apps.salary_finance.api_v1.serializers import *
from apps.user_account.models import User
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from rest_framework import status

class StaffSalaryViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalarySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateStaffSalarySerializer 
        return StaffSalarySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gross_salary = serializer.validated_data.get('gross_salary', 0)
        basic = serializer.validated_data.get('basic', 0)

        

        dearness_allowance_percentage = serializer.validated_data.get('dearness_allowance_percentage', 0)
        house_rent_allowance_percentage = serializer.validated_data.get('house_rent_allowance_percentage', 0)

        dearness_allowance = gross_salary * (dearness_allowance_percentage / 100)
        house_rent_allowance = (basic + dearness_allowance) * (house_rent_allowance_percentage / 100)


        serializer.validated_data['dearness_allowance'] = dearness_allowance
        serializer.validated_data['house_rent_allowance'] = house_rent_allowance

        # Perform the creation of the instance
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Product Deleted Successfully"}, status=status.HTTP_200_OK)

