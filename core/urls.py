from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Define API URL patterns for various apps
urlpatterns = [
    path("api/v1/user/", include("apps.user_account.api_v1.api_router", namespace="user_account_api_router_v1")),
    path("api/v1/member/", include("apps.member.api_v1.api_router", namespace="member_api_router_v1")),
    # path("api/v1/electrician/", include("apps.electrician.api_v1.api_router", namespace="electrician_api_router_v1")),
    # path("api/v1/task/", include("apps.task.api_v1.api_router", namespace="task_api_router_v1")),
    # path("api/v1/client/", include("apps.client.api_v1.api_router", namespace="client_api_router_v1")),
    # path("api/v1/dashboard/", include("apps.dashboard.api_v1.api_router", namespace="dashboard_api_router_v1")),
    # path("api/v1/investor/", include("apps.investor.api_v1.api_router", namespace="company_investor_api_router_v1")),
    
]
# Admin URL
urlpatterns += [
    path(settings.ADMIN_URL, admin.site.urls),
]

# Media URLs for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Swagger/OpenAPI documentation configurations
api_info = openapi.Info(
    title="Your API Title",
    default_version='v1',
    description="API Description",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="contact@example.com"),
    license=openapi.License(name="BSD License"),
)

# Schema view for API documentation
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# URLs for Swagger UI, Redoc, and schema JSON
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

# Debug mode URLs
if settings.DEBUG:
    from django.views import defaults as default_views

    # Error pages for debugging
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")}),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found")}),
        path("500/", default_views.server_error),
    ]

    # Debug toolbar URLs
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
