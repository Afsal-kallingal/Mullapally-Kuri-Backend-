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
    search_fields = ['first_name','last_name','phone','shipping_address']

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
    
class TargetViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','customer__first_name']

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
        return Response({"message": "Target Deleted Successfully"}, status=status.HTTP_200_OK)
    
    