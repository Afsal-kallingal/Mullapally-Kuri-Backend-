from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.product.models import *
from apps.product.api_v1.serializers import *
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsProductAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProductViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsProductAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Product Deleted Successfully"}, status=status.HTTP_200_OK)


class ProductCategoryViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsProductAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Product Category Deleted Successfully"}, status=status.HTTP_200_OK)

class ProductBrandViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = ProductBrand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsProductAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Product Category Deleted Successfully"}, status=status.HTTP_200_OK)

class SupplierViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            permission_classes = [IsAdmin | IsProductAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Supplier      Deleted Successfully"}, status=status.HTTP_200_OK)
