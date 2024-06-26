from django.conf import settings
from django.urls import path
from django.urls import path
from apps.staff.api_v1.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('staff', StaffViewSet, basename='staff-viewset'),
router.register('designation', DesignationViewSet, basename='designation-viewset'),
router.register('work-roles', WorkRoleViewSet, basename='workrole-viewset'),
router.register('departments', DepartmentViewSet, basename='department-viewset'),
router.register('office-locations', OfficeLocationViewSet, basename='officelocation-viewset'),
router.register('sites', SiteViewSet, basename='site-viewset'),
router.register("country",CountryViewSet,basename='country-viewset'),
router.register("state",StateViewSet,basename='state-viewset'),
router.register("district",DistrictViewSet,basename='district-viewset'),
router.register('customer',CustomerViewSet, basename='customer-viewset'),


# router.register('reports-to', ReportToViewSet, basename='reportto-viewset')
# router.register("tudo",TudoViewSet,basename='tudo'),



urlpatterns = [
    # path("investors/", InvestorListCreateAPIView.as_view(), name="investor-list-create"),
]

app_name = "api_v1"
urlpatterns += router.urls
