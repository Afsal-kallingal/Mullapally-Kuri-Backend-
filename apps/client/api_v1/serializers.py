from apps.main.serializers import BaseModelSerializer
from apps.client.models import *
from apps.user_account.functions import validate_phone
from rest_framework import serializers
from apps.user_account.models import User


class ClientSerializer(BaseModelSerializer):
    assigned_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    profile_photo = serializers.ImageField(required=False)

    class Meta:
        model = Client
        fields = [
            'id', 'full_name', 'address_line', 'district', 'postal_code', 'email',
            'phone', 'emergency_phone', 'gst_number', 'client_type', 'company_name',
            'job_title', 'industry', 'followup_date', 'followup_time', 'notes',
            'latitude', 'longitude', 'google_maps_url', 'assigned_user', 'profile_photo'
        ]

class ClientInteractionSerializer(BaseModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all(), required=False, allow_null=True)

    class Meta:
        model = ClientInteraction
        fields = '__all__'

class ServiceRequestSerializer(BaseModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.customer_contact = validated_data.get('customer_contact', instance.customer_contact)
        instance.customer_address = validated_data.get('customer_address', instance.customer_address)
        instance.request_description = validated_data.get('request_description', instance.request_description)
        instance.preferred_service_date = validated_data.get('preferred_service_date', instance.preferred_service_date)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.location_share_url = validated_data.get('location_share_url', instance.location_share_url)
        instance.followed_up_by = validated_data.get('followed_up_by', instance.followed_up_by)
        instance.follow_up_date = validated_data.get('follow_up_date', instance.follow_up_date)
        instance.save()
        return instance