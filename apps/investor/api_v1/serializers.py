from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.investor.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User



class CreateInvestorSerializer(BaseModelSerializer):
    full_name = serializers.CharField(max_length=128, write_only=True)
    country_code = serializers.IntegerField(write_only=True)
    phone = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Investor
        fields = ['id','full_name', 'phone', 'country_code','email', 'address_line1','certificate_number', 'address_line2', 'post_office', 'district', 'pincode',
                  'share_number', 'bank_holder_name', 'bank_name', 'bank_branch', 'bank_account_number',
                  'bank_ifsc', 'number_of_shares','dob', 'rewards', 'dividend', 'id_proof_type',
                  'id_proof_number', 'nominee_name', 'nominee_address_line1', 'nominee_address_line2',
                  'nominee_id_proof_type', 'nominee_id_proof_number', 'nominee_mobile', 'nominee_country_code', 'nominee_district',
                  'nominee_email','nominee_postoffice','nominee_pincode']
        
    def create(self, validated_data):
            full_name = validated_data.pop('full_name', None)
            country_code = validated_data.pop('country_code', None)
            phone = validated_data.pop('phone', None)
            email = validated_data.pop('email', None)
            if(validate_phone(country_code,phone)):
                user_account = User.objects.create(
                    full_name=full_name,
                    country_code=country_code,
                    phone=phone,
                    email=email,
                    username=str(str(country_code)+str(phone)),
                    phone_verified=True
                    
                    )
                validated_data["user"] = user_account
                instance = super().create(validated_data)
            else:
                instance = Investor.objects.none
                raise serializers.ValidationError("Phone number already exists !")
            
            return instance
    
class InvestorSerializer(BaseModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    phone = serializers.CharField(source='user.phone')
    country_code = serializers.CharField(source='user.country_code')
    email = serializers.CharField(source='user.email')
    country = serializers.CharField(source='district.state.country.id',read_only=True)
    state = serializers.CharField(source='district.id',read_only=True)
    state_name = serializers.CharField(source='district.state.name',read_only=True)
    district_name = serializers.CharField(source='district.name',read_only=True)
    country_name = serializers.CharField(source='district.state.country.name',read_only=True)
    nominee_district_name = serializers.CharField(source='nominee_district.name',read_only=True)
    nominee_state_name = serializers.CharField(source='nominee_district.state.name',read_only=True)

    class Meta:
        model = Investor
        fields = ['id','full_name', 'phone', 'country_code','email', 'address_line1', 'address_line2','certificate_number', 'post_office', 'country', 'state','state_name','district_name','country_name', 'district', 'pincode',
                  'share_number', 'bank_holder_name', 'bank_name', 'bank_branch', 'bank_account_number','date_added',
                  'bank_ifsc', 'number_of_shares','dob', 'rewards', 'dividend', 'id_proof_type',
                  'id_proof_number', 'nominee_name', 'nominee_address_line1', 'nominee_address_line2',
                  'nominee_id_proof_type', 'nominee_id_proof_number', 'nominee_mobile', 'nominee_country_code', 'nominee_district','nominee_district_name','nominee_state_name',
                  'nominee_email','nominee_postoffice','nominee_pincode']

    def update(self, instance, validated_data):
        instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
        instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
        instance.post_office = validated_data.get('post_office', instance.post_office)
        # instance.country = validated_data.get('country', instance.country)
        # instance.state = validated_data.get('state', instance.state)
        instance.district = validated_data.get('district', instance.district)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.share_number = validated_data.get('share_number', instance.share_number)
        instance.bank_holder_name = validated_data.get('bank_holder_name', instance.bank_holder_name)
        instance.bank_name = validated_data.get('bank_name', instance.bank_name)
        instance.bank_branch = validated_data.get('bank_branch', instance.bank_branch)
        instance.bank_account_number = validated_data.get('bank_account_number', instance.bank_account_number)
        instance.bank_ifsc = validated_data.get('bank_ifsc', instance.bank_ifsc)
        instance.number_of_shares = validated_data.get('number_of_shares', instance.number_of_shares)
        # instance.benefits = validated_data.get('benefits', instance.benefits)
        instance.rewards = validated_data.get('rewards', instance.rewards)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.certificate_number = validated_data.get('certificate_number', instance.certificate_number)
        instance.dividend = validated_data.get('dividend', instance.dividend)
        instance.id_proof_type = validated_data.get('id_proof_type', instance.id_proof_type)
        instance.id_proof_number = validated_data.get('id_proof_number', instance.id_proof_number)
        instance.nominee_name = validated_data.get('nominee_name', instance.nominee_name)
        instance.nominee_address_line1 = validated_data.get('nominee_address_line1', instance.nominee_address_line1)
        instance.nominee_postoffice = validated_data.get('nominee_postoffice', instance.nominee_postoffice)
        instance.nominee_pincode = validated_data.get('nominee_pincode', instance.nominee_pincode)
        instance.nominee_address_line2 = validated_data.get('nominee_address_line2', instance.nominee_address_line2)
        instance.nominee_id_proof_type = validated_data.get('nominee_id_proof_type', instance.nominee_id_proof_type)
        instance.nominee_id_proof_number = validated_data.get('nominee_id_proof_number', instance.nominee_id_proof_number)
        instance.nominee_mobile = validated_data.get('nominee_mobile', instance.nominee_mobile)
        instance.nominee_country_code = validated_data.get('nominee_country_code', instance.nominee_country_code)
        instance.nominee_email = validated_data.get('nominee_email', instance.nominee_email)
        instance.nominee_district = validated_data.get('nominee_district', instance.nominee_district)

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



# class LimitedInvestorSerializer(BaseModelSerializer):
#     full_name = serializers.CharField(max_length=128, write_only=True)
#     country_code = serializers.IntegerField(write_only=True)
#     phone = serializers.IntegerField(write_only=True)
#     class Meta:
#         model = Investor
#         fields = ['full_name','country_code','phone','number_of_shares','dividend','share_number','rewards']
    
#     def create(self, validated_data):
#         full_name = validated_data.pop('full_name', None)
#         country_code = validated_data.pop('country_code', None)
#         phone = validated_data.pop('phone', None)
#         if(validate_phone(country_code,phone)):
#             user_account = User.objects.create(
#                 full_name=full_name,
#                 country_code=country_code,
#                 phone=phone,
#                 username=str(str(country_code)+str(phone)),
#                 phone_verified=True
#                 )
#             validated_data["user"] = user_account
#             instance = super().create(validated_data)
#         else:
#             instance = Investor.objects.none
#             raise serializers.ValidationError("Phone number already exists !")
          
#         return instance
    


# class UpdateInvestorSerializer(BaseModelSerializer):
#     full_name = serializers.CharField(source='user.full_name')
#     phone = serializers.CharField(source='user.phone')
#     country_code = serializers.CharField(source='user.country_code')
#     email = serializers.CharField(source='user.email')
#     country = serializers.CharField(source='district.state.country.id',read_only=True)
#     state = serializers.CharField(source='district.id',read_only=True)
#     state_name = serializers.CharField(source='district.state.name',read_only=True)
#     district_name = serializers.CharField(source='district.name',read_only=True)
#     country_name = serializers.CharField(source='district.state.country.name',read_only=True)
#     nominee_district_name = serializers.CharField(source='nominee_district.name',read_only=True)
#     nominee_state_name = serializers.CharField(source='nominee_district.state.name',read_only=True)
#     # certificate_number = serializers.CharField(source='Investor.certificate_number',read_only=True)
    

#     class Meta:
#         model = Investor
#         # fields = [
#         #     'id','full_name', 'email', 'address_line1', 'address_line2', 'post_office', 'country', 'state',
#         #     'state_name', 'district_name', 'country_name', 'district', 'pincode', 'bank_holder_name', 'bank_name', 
#         #     'bank_branch', 'bank_account_number', 'date_added', 'bank_ifsc', 'dob', 'id_proof_type', 'id_proof_number', 
#         #     'nominee_name', 'nominee_address_line1', 'nominee_address_line2', 'nominee_id_proof_type', 
#         #     'nominee_id_proof_number', 'nominee_mobile', 'nominee_country_code', 'nominee_district', 'nominee_email'
#         # ]
#         fields = ['id','full_name', 'phone', 'country_code','email', 'address_line1', 'address_line2','certificate_number', 'post_office', 'country', 'state','state_name','district_name','country_name', 'district', 'pincode',
#             'share_number', 'bank_holder_name', 'bank_name', 'bank_branch', 'bank_account_number','date_added',
#             'bank_ifsc', 'number_of_shares','dob', 'rewards', 'dividend', 'id_proof_type',
#             'id_proof_number', 'nominee_name', 'nominee_address_line1', 'nominee_address_line2',
#             'nominee_id_proof_type', 'nominee_id_proof_number', 'nominee_mobile', 'nominee_country_code', 'nominee_district','nominee_district_name','nominee_state_name',
#             'nominee_email','nominee_postoffice','nominee_pincode']

#     def update(self, instance, validated_data):
#         user_data = validated_data.pop('user', {})
#         if user_data:
#             user = instance.user
#             user.full_name = user_data.get('full_name', user.full_name)
#             user.email = user_data.get('email', user.email)
#             user.save()

#         # Handle other fields
#         instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
#         instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
#         instance.post_office = validated_data.get('post_office', instance.post_office)
#         instance.district = validated_data.get('district', instance.district)
#         instance.pincode = validated_data.get('pincode', instance.pincode)
#         instance.bank_holder_name = validated_data.get('bank_holder_name', instance.bank_holder_name)
#         instance.bank_name = validated_data.get('bank_name', instance.bank_name)
#         instance.bank_branch = validated_data.get('bank_branch', instance.bank_branch)
#         instance.bank_account_number = validated_data.get('bank_account_number', instance.bank_account_number)
#         instance.bank_ifsc = validated_data.get('bank_ifsc', instance.bank_ifsc)
#         instance.dob = validated_data.get('dob', instance.dob)
#         instance.id_proof_type = validated_data.get('id_proof_type', instance.id_proof_type)
#         instance.id_proof_number = validated_data.get('id_proof_number', instance.id_proof_number)
#         instance.nominee_name = validated_data.get('nominee_name', instance.nominee_name)
#         instance.nominee_address_line1 = validated_data.get('nominee_address_line1', instance.nominee_address_line1)
#         instance.nominee_address_line2 = validated_data.get('nominee_address_line2', instance.nominee_address_line2)
#         instance.nominee_id_proof_type = validated_data.get('nominee_id_proof_type', instance.nominee_id_proof_type)
#         instance.nominee_id_proof_number = validated_data.get('nominee_id_proof_number', instance.nominee_id_proof_number)
#         instance.nominee_mobile = validated_data.get('nominee_mobile', instance.nominee_mobile)
#         instance.nominee_country_code = validated_data.get('nominee_country_code', instance.nominee_country_code)
#         instance.nominee_email = validated_data.get('nominee_email', instance.nominee_email)
#         instance.nominee_district = validated_data.get('nominee_district', instance.nominee_district)

#         # Save the updated instance
#         instance.save()
#         return instance
   
#         # serialized_instance = InvestorSerializer(instance)
#         # return serialized_instance
            

class CompanySerializer(BaseModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'company_description', 'terms', 'benefits']
        extra_kwargs = {
            'company_name': {'required': False},
            'company_description': {'required': False},
            'terms': {'required': False},
            'benefits': {'required': False},
        }


