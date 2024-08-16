# from apps.main.serializers import BaseModelSerializer
# from apps.client.models import *
# from apps.user_account.functions import validate_phone
# from rest_framework import serializers
# from apps.user_account.models import User


# class ClientSerializer(BaseModelSerializer):
#     assigned_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
#     profile_photo = serializers.ImageField(required=False)

#     class Meta:
#         model = Client
#         fields = [
#             'id', 'full_name', 'address_line', 'district', 'postal_code', 'email',
#             'phone', 'emergency_phone', 'gst_number', 'client_type', 'company_name',
#             'job_title', 'industry', 'followup_date', 'followup_time', 'notes',
#             'latitude', 'longitude', 'google_maps_url', 'assigned_user', 'profile_photo'
#         ]

# class ClientInteractionSerializer(BaseModelSerializer):
#     client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
#     staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all(), required=False, allow_null=True)

#     class Meta:
#         model = ClientInteraction
#         fields = '__all__'