from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.investor.models import *
from apps.investor.api_v1.serializers import *
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# class InvestorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Investor.objects.all()
#     serializer_class = InvestorSerializer

class InvestorViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['share_number','user__full_name','address_line1','address_line2','user__phone','bank_name','nominee_name','user__email']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateInvestorSerializer
            # return LimitedInvestorSerializer
        else:
            return InvestorSerializer
        
    # def get_queryset(self):
    #     queryset =  Investor.objects.all()
    #     if "district" in self.request.GET:
    #         queryset = queryset.filter(district=self.request.GET.get("district"))
    #     if "state" in self.request.GET:
    #         queryset = queryset.filter(district__state=self.request.GET.get("state"))
    #     if "country" in self.request.GET:
    #         queryset = queryset.filter(district__state__country=self.request.GET.get("country"))
    #     if "pincode" in self.request.GET:
    #         queryset = queryset.filter(pincode=self.request.GET.get("pincode"))
    #     if self.request.GET.get('start_date'):
    #         queryset = queryset.filter(date_added__gte=self.request.GET.get("start_date"))
    #     if self.request.GET.get('end_date'):
    #         queryset = queryset.filter(date_added__lte=self.request.GET.get("end_date"))
    #     return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        instance.share_number = "SNH"+str(format(instance.auto_id, '03'))
        instance.save()
        serializer2= InvestorSerializer(instance=instance)
        # Investor.objects.filter(id=serializer.data["id"]).update(share_number="SNH"+str(serializer.data["auto_id"]))
        return Response(serializer2.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     request_data = request.data.copy()
    #     serializer = self.get_serializer(instance, data=request_data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Invester Account Deleted Successfully"}, status=status.HTTP_200_OK)
    
    # district = openapi.Parameter('district', openapi.IN_QUERY,description="district",type=openapi.TYPE_STRING)
    # state = openapi.Parameter('state', openapi.IN_QUERY,description="state",type=openapi.TYPE_STRING)
    # country = openapi.Parameter('country', openapi.IN_QUERY,description="country",type=openapi.TYPE_STRING)
    # pincode = openapi.Parameter('pincode', openapi.IN_QUERY,description="pincode",type=openapi.TYPE_STRING)
    # self_data = openapi.Parameter('self-data', openapi.IN_QUERY,description="get user self data",type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[district,state,country,pincode,self_data])
    # def list(self, request, *args, **kwargs):
    #     if("self-data" in self.request.GET) and (request.GET["self-data"]=="true" or request.GET["self-data"]==True):
    #         instance = self.get_queryset().filter(user=request.user).first()
    #         serializer = self.get_serializer(instance)
    #         return Response(serializer.data)
        
    #     else:
    #         queryset = self.filter_queryset(self.get_queryset())
    #         queryset = self.paginate_queryset(queryset)
    #         if queryset is not None:
    #             serializer = self.get_serializer(queryset, many=True, context={'request': self.request})
    #             return self.get_paginated_response(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_200_OK) 


class CompanyViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['company_name']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def get_object(self):
        # Always return the first (and only) Company object
        return Company.objects.first()
    
    def create(self, request, *args, **kwargs):
        if(not Company.objects.all().exists()):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            partial = kwargs.pop('partial', False)
            instance = Company.objects.all().first()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        # queryset = self.paginate_queryset(self.filter_queryset())
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)
  
    def destroy(self, request, *args, **kwargs):
        Company.objects.all().delete()
        return Response({"message": "Settings deleted successfully"}, status=status.HTTP_200_OK)
    
    # investment = openapi.Parameter('course', openapi.IN_QUERY,description="filter by course",type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[investment])
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     queryset = self.paginate_queryset(queryset)
    #     if queryset is not None:
    #         serializer = self.get_serializer(queryset, many=True, context={'request': self.request})
    #         return self.get_paginated_response(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_200_OK) 

