from django.conf import settings
from django.urls import path
from apps.electrician.api_v1.views import ElectricianViewSet,ElectricianStaffViewSet,ElectricianPointTrackViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('electrician', ElectricianViewSet, basename='electrician-viewset'),
router.register('electrician-staff', ElectricianStaffViewSet, basename='electrician-staff-viewset'),
router.register('electrician-point-tracks', ElectricianPointTrackViewSet, basename='electrician-point-tracks-viewset'),


urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
