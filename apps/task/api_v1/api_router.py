from django.conf import settings
from django.urls import path
from apps.task.api_v1.views import SaleTargetViewSet,SalesmanSalesTargetStatusViewSet,CustomerRelationshipTargetViewSet,SalesmanCustomerRelationshipTargetStatusViewSet,StaffTaskViewSet,SalesmanTaskStatusViewSet,creators_task_listview,creator_task_responce_view,admin_task,CompanyNotesViewset,forward_task,TaskHistoryViewSet
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
router.register('all-note', CompanyNotesViewset, basename='all-staff-notes')
router.register('task-history', TaskHistoryViewSet, basename='task-historyes')

urlpatterns = [
    path('creator-tasks/', creators_task_listview, name='creators-task-list'),
    path('creator-task-status/', creator_task_responce_view, name='creators-task-status-list'),
    path('admin-tasks/', admin_task, name='admin-task-list-view'),
    path('staff-tasks/<uuid:task_id>/forward/', forward_task, name='forward_task'),
]

app_name = "api_v1"
urlpatterns += router.urls
