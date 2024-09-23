from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.member.models import *
from apps.member.api_v1.serializers import *
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# class InvestorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Investor.objects.all()
#     serializer_class = InvestorSerializer

class MemberViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = CreatememberSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__full_name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "member Deleted Successfully"}, status=status.HTTP_200_OK)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreatememberSerializer
        elif self.action == 'update':
            return CreatememberSerializer
        #     else:
        # #         return UpdateInvestorSerializer
        # elif self.action == 'list':
        #     return StafflistSerializer
        else:
            return MemberviewSerializer
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_admin and instance.user != request.user:
            return Response({"detail": "You do not have permission to update this profile."}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

class PaymentViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['member__user__full_name']

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:  
            return Payment.objects.all()
        else:
            return Payment.objects.filter(member__user=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PaymentListSerializer 
        return PaymentSerializer 
