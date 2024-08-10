
from django.conf import settings
from django.urls import path
from apps.dashboard.api_v1.views import task_dashboard,delivery_dashboard,staff_sales_target_summary,sales_and_customer_relationship_dashboard
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register('client', ClientViewSet, basename='client-viewset'),

urlpatterns = [
    path('task/', task_dashboard, name='task-dashboard'),
    path('deliveries/', delivery_dashboard, name='delivery-dashboard'),
    path('sales-target-summary/', staff_sales_target_summary, name='staff_sales_target_summary'),
    path('sales-relationship/', sales_and_customer_relationship_dashboard, name='sales_and_customer_relationship_dashboard-view'),

    ]

app_name = "api_v1"
urlpatterns += router.urls
