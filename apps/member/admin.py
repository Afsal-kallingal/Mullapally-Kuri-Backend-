from django.contrib import admin
from apps.member.models import *



class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','user','nominee_full_name','nominee_relation','nominee_phone','address_line1','address_line2','city','state','country','postal_code','dob','occupation','date_added', 'creator',
    )
admin.site.register(Member,MemberAdmin)

