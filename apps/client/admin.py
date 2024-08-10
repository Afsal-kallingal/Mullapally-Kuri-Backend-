from django.contrib import admin
from apps.client.models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'address_line', 'district', 'postal_code', 'email', 'phone',
        'emergency_phone', 'gst_number', 'client_type', 'company_name', 'job_title',
        'industry', 'followup_date', 'followup_time', 'notes', 'latitude', 'longitude',
        'google_maps_url', 'assigned_user', 'profile_photo'
    )
    search_fields = (
        'full_name', 'address_line', 'district__name', 'postal_code', 'email', 
        'phone', 'emergency_phone', 'gst_number', 'client_type', 'company_name', 
        'job_title', 'industry', 'notes', 'assigned_user__username'
    )
    list_filter = (
        'client_type', 'district', 'followup_date', 'assigned_user'
    )
    readonly_fields = ('google_maps_url',)  # Make the Google Maps URL read-only
    fieldsets = (
        (None, {
            'fields': ('full_name', 'address_line', 'district', 'postal_code', 'email', 
                       'phone', 'emergency_phone', 'gst_number', 'client_type')
        }),
        ('Professional Details', {
            'fields': ('company_name', 'job_title', 'industry')
        }),
        ('Follow-up Details', {
            'fields': ('followup_date', 'followup_time', 'notes')
        }),
        ('Location Details', {
            'fields': ('latitude', 'longitude', 'google_maps_url')
        }),
        ('Assigned User and Photo', {
            'fields': ('assigned_user', 'profile_photo')
        }),
    )

# Register the model with the admin site
admin.site.register(Client, ClientAdmin)
