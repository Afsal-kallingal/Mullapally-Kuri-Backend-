from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.staff.models import *
from apps.user_account.functions import validate_phone
from apps.user_account.models import User



class CreateInvestorSerializer(BaseModelSerializer):
    # full_name = serializers.CharField(max_length=128, write_only=True)
    country_code = serializers.IntegerField(write_only=True)
    phone = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Staff
        fields = ['id','user', 'role', 'sales_target','phone_number', 'email','address', 'active', 'notes']
        
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