from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.client.models import *
from apps.client.api_v1.serializers import *
from rest_framework.filters import SearchFilter


class ClientViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone','full_name']