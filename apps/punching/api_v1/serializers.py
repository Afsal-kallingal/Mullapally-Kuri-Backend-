from apps.main.serializers import BaseModelSerializer
from rest_framework import serializers
from apps.punching.models import Attendance
from apps.user_account.functions import validate_phone



class AttendanceSerializer(BaseModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'id',
            'user',
            'user_full_name',
            'location',
            'time_in',
            'time_out',
            'punch_type',
            'date_added'
        ]

    def get_user_full_name(self, obj):
        return obj.user.full_name