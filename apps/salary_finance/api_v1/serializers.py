from apps.main.serializers import BaseModelSerializer
from apps.salary_finance.models import *
from apps.user_account.functions import validate_phone


class CreateStaffSalarySerializer(BaseModelSerializer):
    class Meta:
        model = StaffSalary
        fields = ['id','user','gross_salary','gross_ctc_company']

class StaffSalarySerializer(BaseModelSerializer):
    class Meta:
        model = StaffSalary
        fields = '__all__'

class StaffSalaryPersontageCalculationsSerializer(BaseModelSerializer):
    class Meta:
        model = StaffSalaryPersontageCalculations
        fields = ['id','dearness_allowance_percentage','house_rent_allowance_percentage']
