from django.contrib import admin
from apps.investor.models import *



class InvestorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address_line1','certificate_number', 'address_line2', 'post_office','district','pincode','share_number','bank_holder_name','bank_name','bank_branch','bank_account_number','bank_ifsc','number_of_shares','dividend','id_proof_type','nominee_name','nominee_address_line1','nominee_district','nominee_postoffice','nominee_pincode',
    )
admin.site.register(Investor,InvestorsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','company_description','terms','benefits')
admin.site.register(Company,CompanyAdmin)

