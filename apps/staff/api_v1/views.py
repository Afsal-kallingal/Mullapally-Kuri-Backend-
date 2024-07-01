from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.staff.models import *
from apps.staff.api_v1.serializers import *
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsStaffAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# class InvestorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Investor.objects.all()
#     serializer_class = InvestorSerializer

class StaffViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','user__full_name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin | IsStaffAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Staff Deleted Successfully"}, status=status.HTTP_200_OK)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateStaffSerializer
        # elif self.action == 'update':
        #     if self.request.user.is_admin:
        #         return InvestorSerializer
        #     else:
        # #         return UpdateInvestorSerializer
        # elif self.action == 'list':
        #     return StafflistSerializer
        else:
            return StaffSerializer
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_admin and instance.user != request.user:
            return Response({"detail": "You do not have permission to update this profile."}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)


class CountryViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    
    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class StateViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = State.objects.filter()
        if "country" in self.request.GET:
            queryset = queryset.filter(country=self.request.GET.get("country"))
        return queryset

class DistrictViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = District.objects.filter()
        if "state" in self.request.GET:
            queryset = queryset.filter(state=self.request.GET.get("state"))
        return queryset

class DesignationViewSet(BaseModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class WorkRoleViewSet(BaseModelViewSet):
    queryset = WorkRole.objects.all()
    serializer_class = WorkRoleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class DepartmentViewSet(BaseModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class OfficeLocationViewSet(BaseModelViewSet):
    queryset = OfficeLocation.objects.all()
    serializer_class = OfficeLocationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['address']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class SiteViewSet(BaseModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

# class ReportToViewSet(BaseModelViewSet):
#     queryset = Report_To.objects.all()
#     serializer_class = ReportToSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name']

#     def get_permissions(self):
#         if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
#             permission_classes = [IsAdmin]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]


class CustomersViewSet(BaseModelViewSet):
    permission_classes = [AllowAny ]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name','phone','shipping_address','auto_id']

    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'destroy':
    #         permission_classes = [IsAdmin | IsTargetAdmin]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Customer Deleted Successfully"}, status=status.HTTP_200_OK)
    