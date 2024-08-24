# from apps.main.serializers import BaseModelSerializer
# from rest_framework import serializers
# from apps.salary_staff.models import *
# from apps.user_account.models import User

# class CreateStaffSalarySerializer(BaseModelSerializer):
#     dearness_allowance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     house_rent_allowance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     conveyance_allowance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     special_allowance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     pf_employer_contribution = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     esi_employer_contribution = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     pf_employee_contribution = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     esi_employee_contribution = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     total_deductions = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     net_salary_payable = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
#     gross_ctc_company = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

#     dearness_allowance_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True)
#     house_rent_allowance_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True)
#     pf_employer_contribution_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True)
#     esi_employer_contribution_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True)
#     pf_employee_contribution_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True)

#     class Meta:
#         model = StaffSalary
#         fields = [
#             'id', 'user', 'gross_salary', 'basic',
#             'dearness_allowance', 'house_rent_allowance', 'conveyance_allowance', 'special_allowance',
#             'pf_employer_contribution', 'esi_employer_contribution', 'pf_employee_contribution',
#             'esi_employee_contribution', 'professional_tax', 'other_deductions', 'total_deductions',
#             'net_salary_payable', 'gross_ctc_company',
#             'dearness_allowance_percentage', 'house_rent_allowance_percentage', 'conveyance_allowance',
#             'pf_employer_contribution_percentage', 'esi_employer_contribution_percentage',
#             'pf_employee_contribution_percentage'
#         ]

#     def validate(self, data):
#         gross_salary = data.get('gross_salary', 0)
#         basic = data.get('basic', 0)
#         dearness_allowance_percentage = data.get('dearness_allowance_percentage', 0)
#         house_rent_allowance_percentage = data.get('house_rent_allowance_percentage', 0)
#         conveyance_allowance = data.get('conveyance_allowance', 0)
#         pf_employer_contribution_percentage = data.get('pf_employer_contribution_percentage', 0)
#         esi_employer_contribution_percentage = data.get('esi_employer_contribution_percentage', 0)
#         pf_employee_contribution_percentage = data.get('pf_employee_contribution_percentage', 0)
#         professional_tax = data.get('professional_tax', 0)
#         other_deductions = data.get('other_deductions', 0)

#         dearness_allowance = gross_salary * (dearness_allowance_percentage / 100)
#         house_rent_allowance = (basic + dearness_allowance) * (house_rent_allowance_percentage / 100)
#         special_allowance = gross_salary - (basic + dearness_allowance + house_rent_allowance + conveyance_allowance)

#         if basic + dearness_allowance > 15000:
#             pf_employer_contribution = 18000 * (pf_employer_contribution_percentage / 100)
#         else:
#             pf_employer_contribution = (basic + dearness_allowance) * (pf_employer_contribution_percentage / 100)

#         esi_employer_contribution = 0 if gross_salary > 21000 else gross_salary * (esi_employer_contribution_percentage / 100)
#         gratuity = basic * (15 / 26) / 12

#         pf_employee_contribution = (18000 if basic > 15000 else basic) * (pf_employee_contribution_percentage / 100)
#         esi_employee_contribution = 0 if gross_salary > 21000 else gross_salary * 0.0075

#         total_deductions = pf_employee_contribution + esi_employee_contribution + professional_tax + other_deductions
#         net_salary_payable = gross_salary - total_deductions
#         gross_ctc_company = gross_salary + pf_employee_contribution + gratuity

#         data['dearness_allowance'] = dearness_allowance
#         data['house_rent_allowance'] = house_rent_allowance
#         data['conveyance_allowance'] = conveyance_allowance
#         data['special_allowance'] = special_allowance
#         data['pf_employer_contribution'] = pf_employer_contribution
#         data['esi_employer_contribution'] = esi_employer_contribution
#         data['pf_employee_contribution'] = pf_employee_contribution
#         data['esi_employee_contribution'] = esi_employee_contribution
#         data['total_deductions'] = total_deductions
#         data['net_salary_payable'] = net_salary_payable
#         data['gross_ctc_company'] = gross_ctc_company

#         return data

# class StaffSalarySerializer(BaseModelSerializer):
#     class Meta:
#         model = StaffSalary
#         fields = '__all__'

# class StaffSalaryPercentageCalculationsSerializer(BaseModelSerializer):
#     class Meta:
#         model = StaffSalaryPercentageCalculations
#         fields = [
#             'dearness_allowance_percentage',
#             'house_rent_allowance_percentage',
#             'conveyance_allowance',
#             'pf_employer_contribution_percentage',
#             'esi_employer_contribution_percentage'
#         ]
