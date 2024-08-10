from django.contrib import admin
from apps.staff.models import *



class StaffAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','address_line','dob','district','salary','rewards','designation','post','department','office_location','site','operating','date_added', 'creator',
    )
admin.site.register(Staff,StaffAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(State,StateAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(District,DistrictAdmin)

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_added', 'creator')
admin.site.register(Designation,DesignationAdmin)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_added', 'creator')
admin.site.register(WorkRole,RolesAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_added', 'creator')
admin.site.register(Department,DepartmentAdmin)

class OfficeLocationAdmin(admin.ModelAdmin):
    list_display = ('id','address','date_added', 'creator')
admin.site.register(OfficeLocation,OfficeLocationAdmin)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_added', 'creator')
admin.site.register(Site,SiteAdmin)



