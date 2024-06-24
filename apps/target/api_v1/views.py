from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.target.models import *
from apps.target.api_v1.serializers import *
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsTargetAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# class InvestorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Investor.objects.all()
#     serializer_class = InvestorSerializer

class CustomerViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name','phone','shipping_address','auto_id']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Customer Deleted Successfully"}, status=status.HTTP_200_OK)
    
class SalesTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = SalesTarget.objects.all()
    serializer_class = SalesTargetSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['salesman','customer__first_name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    # def get_serializer_class(self):
    #     if request.user.is_authenticated and request.user.target_admin:
    #         # return True
    #         return SalesmanSalesTargetUpdateSerializer
    #     return SalesTargetSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Sales Target Deleted Successfully"}, status=status.HTTP_200_OK)
  
class CustomerRelationshipTargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = CustomerRelationshipTarget.objects.all()
    serializer_class = CustomerRelationshipTargetSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['salesman','customer__first_name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin | IsTargetAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Customer Relationship Target Deleted Successfully"}, status=status.HTTP_200_OK)
  
    