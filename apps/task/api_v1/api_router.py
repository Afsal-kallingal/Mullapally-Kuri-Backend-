from django.conf import settings
from django.urls import path
<<<<<<< HEAD
from apps.task.api_v1.views import SaleTargetViewSet,SalesmanSalesTargetStatusViewSet,CustomerRelationshipTargetViewSet,SalesmanCustomerRelationshipTargetStatusViewSet,StaffTaskViewSet,SalesmanTaskStatusViewSet,creators_task_listview,creator_task_responce_view,admin_task,CompanyNotesViewset,forward_task,TaskHistoryViewSet,creator_task_delete_view,DeliveryAreaViewSet,DeliveryViewSet,admin_task_responce_status
=======
from apps.task.api_v1.views import SaleTargetViewSet,SalesmanSalesTargetStatusViewSet,CustomerRelationshipTargetViewSet,SalesmanCustomerRelationshipTargetStatusViewSet,StaffTaskViewSet,SalesmanTaskStatusViewSet,creators_task_listview,creator_task_responce_view,admin_task,CompanyNotesViewset,forward_task,TaskHistoryViewSet,creator_task_delete_view,DeliveryAreaViewSet,DeliveryViewSet,admin_task_responce_status,task_history_detail
>>>>>>> c00bbdfd9808f039165c93db1c29eb841b502646
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
router.register('delivery-area', DeliveryAreaViewSet, basename='delivery-areas')
router.register('delivery', DeliveryViewSet, basename='delivery')


# Register StaffTaskAudioViewSet with a unique basename
urlpatterns = [
    path('creator-tasks/', creators_task_listview, name='creators-task-list'),
    path('creator-task-status/', creator_task_responce_view, name='creators-task-status-list'),
    path('admin-tasks/', admin_task, name='admin-task-list-view'),
    path('admin-tasks-status/', admin_task_responce_status, name='admin-task-status-list-view'),
<<<<<<< HEAD
    path('staff-tasks/<uuid:task_id>/forward/', forward_task, name='forward_task'),
=======
    path('task/<uuid:task_id>/forward/', forward_task, name='forward_task'),
>>>>>>> c00bbdfd9808f039165c93db1c29eb841b502646
    path('tasks/delete/<uuid:task_id>/', creator_task_delete_view, name='creator_task_delete_views'),
    path('task/<uuid:task_id>/history/', task_history_detail, name='task_history_detail'),

]

app_name = "api_v1"
urlpatterns += router.urls

