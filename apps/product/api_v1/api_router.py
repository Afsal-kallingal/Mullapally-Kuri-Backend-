from django.conf import settings
from django.urls import path
from apps.product.api_v1.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('product', ProductViewSet, basename='product-viewset'),
router.register('product-category', ProductCategoryViewSet, basename='product-category-viewset'),
router.register('product-brand', ProductBrandViewSet, basename='product-brand-viewset'),
router.register('product-supplier', SupplierViewSet, basename='product-supplier-viewset'),

urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
