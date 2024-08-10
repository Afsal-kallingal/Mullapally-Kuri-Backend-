from django.conf import settings
from django.urls import path
from apps.client.api_v1.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('client', ClientViewSet, basename='client-viewset'),

urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
