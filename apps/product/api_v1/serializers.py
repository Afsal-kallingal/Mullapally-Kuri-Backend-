from apps.main.serializers import BaseModelSerializer
from apps.product.models import *
from apps.user_account.functions import validate_phone


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
        fields = ['id','name','description','price','cost','profit','taxable_amount','discount_price','stock','product_category','brand','supplier','points','image','updated_at','date_added','creator',]

