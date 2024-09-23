from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.member.models import *
from django.db import IntegrityError
from apps.user_account.functions import validate_phone
from apps.user_account.models import User
from rest_framework.exceptions import ValidationError


class CreatememberSerializer(BaseModelSerializer):
    full_name = serializers.CharField(max_length=128, write_only=True)
    country_code = serializers.CharField(max_length=5, write_only=True)
    phone = serializers.CharField(max_length=15, write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    profile_picture = serializers.ImageField(required=False, write_only=True)  # Add this line

    class Meta:
        model = Member
        fields = [
            'id', 'full_name', 'phone', 'country_code', 'email', 'password', 'nominee_full_name', 'nominee_relation', 
            'nominee_phone', 'address_line1', 'address_line2', 'city', 'state', 'country', 'postal_code', 'dob', 
            'profile_picture', 'occupation'
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

class MemberviewSerializer(BaseModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    phone = serializers.CharField(source='user.phone')
    country_code = serializers.CharField(source='user.country_code')
    email = serializers.CharField(source='user.email')
    profile_picture = serializers.ImageField(required=False, allow_null=True)  # Allow null for optional updates

    class Meta:
        model = Member
        fields = [
            'id', 'full_name', 'phone', 'country_code', 'email', 'nominee_full_name', 'nominee_relation', 
            'nominee_phone', 'address_line1', 'address_line2', 'city', 'state', 'country', 'postal_code', 'dob', 
            'profile_picture', 'occupation'
        ]

    def update(self, instance, validated_data):
        # Update member fields
        instance.nominee_full_name = validated_data.get('nominee_full_name', instance.nominee_full_name)
        instance.nominee_relation = validated_data.get('nominee_relation', instance.nominee_relation)
        instance.nominee_phone = validated_data.get('nominee_phone', instance.nominee_phone)
        instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
        instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.occupation = validated_data.get('occupation', instance.occupation)

        # Update profile picture if provided
        profile_picture = validated_data.get('profile_picture', None)
        if profile_picture:
            instance.profile_picture = profile_picture

        # Update user-related fields
        user_data = validated_data.pop('user', {})
        user = instance.user

        if user_data:
            user.full_name = user_data.get('full_name', user.full_name)
            user.email = user_data.get('email', user.email)
            country_code = user_data.get('country_code', user.country_code)
            phone = user_data.get('phone', user.phone)

            # Check if phone or country_code changes and validate
            if (user.country_code != country_code) or (user.phone != phone):
                if validate_phone(country_code, phone):
                    user.country_code = country_code
                    user.phone = phone
                    user.username = f"{country_code}{phone}"  # Update username based on phone
                else:
                    raise serializers.ValidationError("Phone number already exists or is invalid!")
            
            user.save()

        # Save the updated instance of Member
        instance.save()
        return instance
 
class PaymentSerializer(BaseModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__' 

class PaymentListSerializer(BaseModelSerializer):
    creator_name = serializers.CharField(source='creator.full_name', read_only=True)  # Assuming creator is linked to User model
    member_name = serializers.CharField(source='member.user.full_name', read_only=True)  # Fetching member's full name

    class Meta:
        model = Payment
        fields = ['id', 'creator_name', 'member_name', 'amount', 'payment_method', 'date_added']
