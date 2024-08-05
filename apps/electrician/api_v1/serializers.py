# from apps.main.serializers import BaseModelSerializer
# from apps.electrician.models import Electrician
# from apps.user_account.functions import validate_phone
# from rest_framework import serializers
# from apps.user_account.models import User

# class CreateElectricianSerializer(BaseModelSerializer):
#     full_name = serializers.CharField(max_length=128, write_only=True)
#     country_code = serializers.CharField(max_length=5, write_only=True)
#     phone = serializers.CharField(max_length=15, write_only=True)
#     email = serializers.EmailField(write_only=True)
#     password = serializers.CharField(write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = Electrician
#         fields = [
#             'id', 'full_name', 'phone', 'country_code', 'email', 'password', 'address_line', 'temporary_address_line',
#             'dob', 'district', 'national_id', 'blood_group', 'emergency_contact_name', 'emergency_contact_number', 
#             'health_conditions', 'marital_status', 'spouse_name', 'spouse_dob', 'spouse_occupation', 'father_name', 
#             'mother_name', 'years_of_experience', 'certifications', 'specialization', 'previous_employers', 'skills', 
#             'nominee_name', 'nominee_relation', 'nominee_dob', 'nominee_contact_number', 'nominee_address', 
#             'child1_name', 'child1_dob', 'child1_gender', 'child1_school', 'child2_name', 'child2_dob', 'child2_gender', 
#             'child2_school', 'child3_name', 'child3_dob', 'child3_gender', 'child3_school', 'child4_name', 'child4_dob', 
#             'child4_gender', 'child4_school', 'child5_name', 'child5_dob', 'child5_gender', 'child5_school',
#         ]

#     def create(self, validated_data):
#         full_name = validated_data.pop('full_name', None)
#         country_code = validated_data.pop('country_code', None)
#         phone = validated_data.pop('phone', None)
#         email = validated_data.pop('email', None)
#         password = validated_data.pop('password', None)

#         if validate_phone(country_code, phone):
#             user_account = User(
#                 full_name=full_name,
#                 country_code=country_code,
#                 phone=phone,
#                 email=email,
#                 username=str(country_code) + str(phone),
#                 phone_verified=True
#             )
#             user_account.set_password(password)  # Hash the password
#             user_account.save()

#             # Set the user in the validated_data dictionary to be used by the super().create() call
#             validated_data["user"] = user_account

#             instance = super().create(validated_data)
#         else:
#             raise serializers.ValidationError("Phone number already exists!")
        
#         return instance