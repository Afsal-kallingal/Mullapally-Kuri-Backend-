from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.product.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User

class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class BrandSerializer(BaseModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'

class SupplierSerializer(BaseModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(BaseModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'