
from django.conf import settings
from django.urls import path
from apps.dashboard.api_v1.views import task_dashboard,delivery_dashboard,staff_sales_target_summary,sales_and_customer_relationship_dashboard,client_dashboard_report,staff_customer_relationship_summary

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
    path('sales/', sales_and_customer_relationship_dashboard, name='sales_and_customer_relationship_dashboard-view'),
    path('field-staff/', staff_customer_relationship_summary, name='staff_customer_relationship_summary-dashboard'),#staff view
    path('client/', client_dashboard_report, name='client_dashboard_reports'),

    ]

app_name = "api_v1"
urlpatterns += router.urls
