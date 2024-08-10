
from django.conf import settings
from django.urls import path
from apps.dashboard.api_v1.views import task_dashboard,delivery_dashboard
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register('client', ClientViewSet, basename='client-viewset'),

urlpatterns = [
    path('task/', task_dashboard, name='task-dashboard'),
    path('deliveries/', delivery_dashboard, name='delivery-dashboard'),
    ]

app_name = "api_v1"
urlpatterns += router.urls
