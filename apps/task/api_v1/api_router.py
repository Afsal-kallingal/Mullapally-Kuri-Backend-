from django.conf import settings
from django.urls import path
from apps.task.api_v1.views import SaleTargetViewSet,SalesmanSalesTargetStatusViewSet,CustomerRelationshipTargetViewSet,SalesmanCustomerRelationshipTargetStatusViewSet,StaffTaskViewSet,SalesmanTaskStatusViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register('sales-targets', SalesTargetViewSet, basename='sales-target')
router.register('sales-target', SaleTargetViewSet, basename='sale-target')
router.register('sales-target-status', SalesmanSalesTargetStatusViewSet, basename='sales-target-status')
router.register('customer-relationship-targets', CustomerRelationshipTargetViewSet, basename='customer-relationship-target')
router.register('customer-relationship-status', SalesmanCustomerRelationshipTargetStatusViewSet, basename='customer-relationship-status')
router.register('staff-tasks', StaffTaskViewSet, basename='staff-task')
router.register('staff-task-status', SalesmanTaskStatusViewSet, basename='staff-task-status')

urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
