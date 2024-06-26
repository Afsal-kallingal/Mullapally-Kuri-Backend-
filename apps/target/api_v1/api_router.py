from django.conf import settings
from django.urls import path
from apps.target.api_v1.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('sales-target',SalesTargetViewSet, basename='sales-target'),
router.register('customer-relationship-target',CustomerRelationshipTargetViewSet, basename='customer-relationship-target'),
router.register('task',StaffDailyTaskViewSet, basename='task'),


urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
