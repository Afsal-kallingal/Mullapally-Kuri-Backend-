# from django.db import models
# from apps.user_account.models import User
# from apps.main.models import BaseModel

# class StaffSalary(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salaries')
#     basic = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     dearness_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     house_rent_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     special_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     gross_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     pf_employer_contribution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     esi_employer_contribution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     gratuity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     gross_ctc_company = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     pf_employee_contribution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     esi_employee_contribution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     professional_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     other_deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
#     total_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     net_salary_payable = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     class Meta:
#         verbose_name = 'Staff Salary'
#         verbose_name_plural = 'Staff Salaries'

#     def __str__(self):
#         return f"{self.user.username} - {self.gross_salary}"

# class StaffSalaryPercentageCalculations(BaseModel):
#     dearness_allowance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     house_rent_allowance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     conveyance_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     pf_employer_contribution_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     esi_employer_contribution_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)


    