from django.conf import settings
from django.urls import path
from apps.sales_target.api_v1.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('sales-targets', SalesTargetViewSet, basename='sales-target')
router.register('sales-target-status', StaffSalesTargetStatusViewSet, basename='sales-target-status')
router.register('customer-relationship-targets', CustomerRelationshipTargetViewSet, basename='customer-relationship-target')
router.register('customer-relationship-status', StaffCustomerRelationshipstatusViewSet, basename='customer-relationship-status')
router.register('staff-tasks', TaskViewSet, basename='staff-task')
router.register('staff-task-status', StaffTaskViewSet, basename='staff-task-status')

urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
