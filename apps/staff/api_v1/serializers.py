from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.staff.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User



class CreateStaffSerializer(BaseModelSerializer):
    # full_name = serializers.CharField(max_length=128, write_only=True)
    country_code = serializers.IntegerField(write_only=True)
    phone_number = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Staff
        fields = ['id','user', 'first_name', 'phone_number','address_line', 'salary','designation', 'post', 'reports_to','department','office_location','site','operating',]
        
    def create(self, validated_data):
            # full_name = validated_data.pop('full_name', None)
            country_code = validated_data.pop('country_code', None)
            phone = validated_data.pop('phone', None)
            email = validated_data.pop('email', None)
            if(validate_phone(country_code,phone)):
                user_account = User.objects.create(
                    # full_name=full_name,
                    country_code=country_code,
                    phone=phone,
                    email=email,
                    username=str(str(country_code)+str(phone)),
                    phone_verified=True
                    )
                validated_data["user"] = user_account
                instance = super().create(validated_data)
            else:
                instance = Staff.objects.none
                raise serializers.ValidationError("Phone number already exists !")
            
            return instance
    

class StaffSerializer(BaseModelSerializer):
    first_name = serializers.CharField(source='user.full_name')
    phone = serializers.CharField(source='user.phone')
    country_code = serializers.CharField(source='user.country_code')
    email = serializers.CharField(source='user.email')
    # country = serializers.CharField(source='district.state.country.id',read_only=True)
    # state = serializers.CharField(source='district.id',read_only=True)
    state_name = serializers.CharField(source='district.state.name',read_only=True)
    district_name = serializers.CharField(source='district.name',read_only=True)
    country_name = serializers.CharField(source='district.state.country.name',read_only=True)
    # nominee_district_name = serializers.CharField(source='nominee_district.name',read_only=True)
    # nominee_state_name = serializers.CharField(source='nominee_district.state.name',read_only=True)

    class Meta:
        model = Staff
        fields = ['id','first_name','last_name','email','country_code','phone_number','address_line','dob','district','salary','rewards','designation','post','reports_to','department','office_location','site','operating',]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address_line = validated_data.get('address_line', instance.address_line)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.district = validated_data.get('district', instance.district)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.rewards = validated_data.get('rewards', instance.rewards)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.role = validated_data.get('role', instance.role)
        instance.reports_to = validated_data.get('reports_to', instance.reports_to)
        instance.department = validated_data.get('department', instance.department)
        instance.office_location = validated_data.get('office_location', instance.office_location)
        instance.site = validated_data.get('site', instance.site)
        instance.operating = validated_data.get('operating', instance.operating)
        # instance.description = validated_data.get('description', instance.description)
        # instance.benefits = validated_data.get('benefits', instance.benefits)
        # Update user fields
        user_data = validated_data.pop('user', {})  # Extract user data if provided
        user = instance.user
        if user_data:
            user.full_name = user_data.get('full_name', user.full_name)
            user.email = user_data.get('email', user.email)
            country_code = user_data.get('country_code', user.country_code)
            phone = user_data.get('phone', user.phone)
            email = user_data.get('email', user.email)
            if((user.country_code != country_code) or (user.phone != phone) and validate_phone(country_code,phone)):
                user.phone = phone
                user.email = email
                user.country_code = country_code
                user.username = str(country_code)+str(phone)
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
        model = Work_Role
        fields = '__all__'

class DepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class OfficeLocationSerializer(BaseModelSerializer):
    class Meta:
        model = OfficeLocation
        fields = '__all__'

class SiteSerializer(BaseModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class ReportToSerializer(BaseModelSerializer):
    class Meta:
        model = Report_To
        fields = '__all__'