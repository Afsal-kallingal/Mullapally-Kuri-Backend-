from django.contrib import admin
from apps.electrician.models import *

class ElectricianAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'address_line', 'temporary_address_line', 'dob', 'district', 
        'national_id', 'blood_group', 'emergency_contact_name', 'emergency_contact_number', 
        'health_conditions', 'marital_status', 'spouse_name', 'spouse_dob', 'spouse_occupation', 
        'father_name', 'mother_name', 'years_of_experience', 'certifications', 
        'specialization', 'previous_employers', 'skills', 'nominee_name', 
        'nominee_relation', 'nominee_dob', 'nominee_contact_number', 'nominee_address', 
        'child1_name', 'child1_dob', 'child1_gender', 'child1_school', 
        'child2_name', 'child2_dob', 'child2_gender', 'child2_school', 
        'child3_name', 'child3_dob', 'child3_gender', 'child3_school', 
        'child4_name', 'child4_dob', 'child4_gender', 'child4_school', 
        'child5_name', 'child5_dob', 'child5_gender', 'child5_school'
    ]

class ElectricianStaffAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'electrician', 'address_line', 'temporary_address_line', 'dob', 'district', 
        'national_id', 'blood_group', 'emergency_contact_name', 'emergency_contact_number', 
        'health_conditions', 'marital_status', 'spouse_name', 'spouse_dob', 'spouse_occupation', 
        'father_name', 'mother_name', 'years_of_experience', 'certifications', 
        'specialization', 'previous_employers', 'skills', 'nominee_name', 
        'nominee_relation', 'nominee_dob', 'nominee_contact_number', 'nominee_address', 
        'child1_name', 'child1_dob', 'child1_gender', 'child1_school', 
        'child2_name', 'child2_dob', 'child2_gender', 'child2_school', 
        'child3_name', 'child3_dob', 'child3_gender', 'child3_school', 
        'child4_name', 'child4_dob', 'child4_gender', 'child4_school', 
        'child5_name', 'child5_dob', 'child5_gender', 'child5_school'
    ]

admin.site.register(Electrician, ElectricianAdmin)
admin.site.register(ElectricianStaff, ElectricianStaffAdmin)
