from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.punching.models import Attendance
from apps.punching.api_v1.serializers import AttendanceSerializer
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
# from apps.user_account.models import User
# from rest_framework.filters import SearchFilter
# from apps.user_account.functions import IsAdmin
# from apps.main.permissions import IsProductAdmin
# from rest_framework import status
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi


class AttendanceViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=False, methods=['post'])
    def punch_in(self, request):
        user = request.user
        location = request.data.get('location')
        punch_type = request.data.get('punch_type', 'ESSL')

        if not location:
            return Response({'error': 'Location is required'}, status=status.HTTP_400_BAD_REQUEST)

        attendance = Attendance.objects.create(
            user=user,
            location=location,
            time_in=timezone.now(),
            punch_type=punch_type
        )
        serializer = self.get_serializer(attendance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def punch_out(self, request, pk=None):
        try:
            attendance = self.get_object()
        except Attendance.DoesNotExist:
            return Response({'error': 'Attendance record not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if attendance.time_out:
            return Response({'error': 'Already punched out'}, status=status.HTTP_400_BAD_REQUEST)
        
        attendance.time_out = timezone.now()
        attendance.save()
        serializer = self.get_serializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)