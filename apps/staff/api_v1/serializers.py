from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.staff.models import *
from django.db import IntegrityError
from apps.user_account.functions import validate_phone
from apps.user_account.models import User
from rest_framework.exceptions import ValidationError


class CreateStaffSerializer(BaseModelSerializer):
    full_name = serializers.CharField(max_length=128, write_only=True)
    country_code = serializers.CharField(max_length=5, write_only=True)
    phone = serializers.CharField(max_length=15, write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    profile_picture = serializers.ImageField(required=False, write_only=True)  # Add this line

    class Meta:
        model = Staff
        fields = [
            'id', 'full_name', 'phone', 'country_code', 'email', 'password', 'address_line', 'dob', 'district', 
            'salary', 'rewards', 'designation', 'post', 'department', 'office_location', 'site', 'operating', 'profile_picture'
        ]

    def create(self, validated_data):
        full_name = validated_data.pop('full_name', None)
        country_code = validated_data.pop('country_code', None)
        phone = validated_data.pop('phone', None)
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        profile_picture = validated_data.pop('profile_picture', None)

        if validate_phone(country_code, phone):
            user_account = User(
                full_name=full_name,
                country_code=country_code,
                phone=phone,
                email=email,
                username=str(str(country_code) + str(phone)),
                phone_verified=True
            )
            user_account.set_password(password)  # Hash the password
            user_account.save()

            # Set the user in the validated_data dictionary to be used by the super().create() call
            validated_data["user"] = user_account

            instance = super().create(validated_data)
            
            # Handle the profile picture
            if profile_picture:
                instance.profile_picture = profile_picture
                instance.save()
        else:
            raise serializers.ValidationError("Phone number already exists!")

        return instance

class StaffSerializer(BaseModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    phone = serializers.CharField(source='user.phone')
    country_code = serializers.CharField(source='user.country_code')
    email = serializers.CharField(source='user.email')
    profile_picture = serializers.ImageField(required=False, allow_null=True)  # Allow null for optional updates
    
    state_name = serializers.CharField(source='district.state.name', read_only=True)
    designation_name = serializers.CharField(source='designation.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    country_name = serializers.CharField(source='district.state.country.name', read_only=True)

    class Meta:
        model = Staff
        fields = [
            'id', 'full_name', 'email', 'country_code', 'phone', 'designation_name', 'state_name',
            'district_name', 'country_name', 'address_line', 'dob', 'district', 'salary', 'rewards',
            'designation', 'post', 'department', 'office_location', 'site', 'operating', 'profile_picture'
        ]

    def update(self, instance, validated_data):
        # Update basic fields
        instance.address_line = validated_data.get('address_line', instance.address_line)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.district = validated_data.get('district', instance.district)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.rewards = validated_data.get('rewards', instance.rewards)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.post = validated_data.get('post', instance.post)
        instance.department = validated_data.get('department', instance.department)
        instance.office_location = validated_data.get('office_location', instance.office_location)
        instance.site = validated_data.get('site', instance.site)
        instance.operating = validated_data.get('operating', instance.operating)

        # Update profile picture if provided
        profile_picture = validated_data.get('profile_picture', None)
        if profile_picture:
            instance.profile_picture = profile_picture

        # Update user fields
        user_data = validated_data.pop('user', {})
        user = instance.user
        if user_data:
            user.full_name = user_data.get('full_name', user.full_name)
            user.email = user_data.get('email', user.email)
            country_code = user_data.get('country_code', user.country_code)
            phone = user_data.get('phone', user.phone)
            email = user_data.get('email', user.email)
            if (user.country_code != country_code) or (user.phone != phone) and validate_phone(country_code, phone):
                user.phone = phone
                user.email = email
                user.country_code = country_code
                user.username = str(country_code) + str(phone)
            user.save()

        # Save the updated instance
        instance.save()
        return instance
       
class DistrictSerializer(BaseModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class StateSerializer(BaseModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = '__all__'

class CountrySerializer(BaseModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'

class DesignationSerializer(BaseModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class WorkRoleSerializer(BaseModelSerializer):
    class Meta:
        model = WorkRole
        fields = '__all__'

class DepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as e:
            raise ValidationError({"detail": str(e)})

class OfficeLocationSerializer(BaseModelSerializer):
    class Meta:
        model = OfficeLocation
        fields = '__all__'

    # def create(self, validated_data):
    #     officelocation = OfficeLocation.objects.create(
    #         **validated_data,
    #         auto_id = get_auto_id(OfficeLocation),
    #         creator = self.context['request'].user
    #     )
    #     return zakat
    
class SiteSerializer(BaseModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

# class ReportToSerializer(BaseModelSerializer):
#     class Meta:
#         model = Report_To
#         fields = '__all__'

# class CustomerSerializer(BaseModelSerializer):
#     class Meta:
#         model = Customer
#         fields = [
#             'id', 'full_name', 'email','phone','phone_number2','billing_address',
#             'shipping_address', 'customer_type', 'tax_id', 'notes', 'is_active', 
#         ]

    # def create(self, validated_data):
    #     full_name = validated_data.pop('full_name', None)
    #     country_code = validated_data.pop('country_code', None)
    #     phone = validated_data.pop('phone', None)
    #     email = validated_data.pop('email', None)
    #     password = validated_data.pop('password', None)

    #     if validate_phone(country_code, phone):
    #         user_account = User(
    #             full_name=full_name,
    #             country_code=country_code,
    #             phone=phone,
    #             email=email,
    #             username=str(str(country_code) + str(phone)),
    #             phone_verified=True
    #         )
    #         user_account.set_password(password)  # Hash the password
    #         user_account.save()

    #         # Set the user in the validated_data dictionary to be used by the super().create() call
    #         validated_data["user"] = user_account

    #         instance = super().create(validated_data)
    #     else:
    #         raise serializers.ValidationError("Phone number already exists!")

    #     return instance