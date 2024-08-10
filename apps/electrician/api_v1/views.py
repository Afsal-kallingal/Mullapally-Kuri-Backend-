from rest_framework import generics
from rest_framework.response import Response
from apps.main.viewsets import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.electrician.models import *
from apps.electrician.api_v1.serializers import *
from apps.user_account.models import User
from rest_framework.filters import SearchFilter
from apps.user_account.functions import IsAdmin
from apps.main.permissions import IsProductAdmin
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework.decorators import api_view,parser_classes,permission_classes,authentication_classes
from rest_framework.parsers import JSONParser,FormParser, MultiPartParser,FileUploadParser
from apps.user_account.functions import validate_username,validate_email,IsAdmin,send_phone_otp,send_email_otp,validate_phone,random_password,save_login_history,fetch_user_by_phone,update_user_token,register_user_by_phone,set_user_token,delete_user_token
from django.contrib.sessions.backends.db import SessionStore


# @api_view(['POST',])
# @permission_classes((AllowAny, ))
# # @authentication_classes([SessionAuthentication])
# @parser_classes([JSONParser, FormParser, MultiPartParser, FileUploadParser])
# def electrician_registration_phone(request):
#     status_code = status.HTTP_400_BAD_REQUEST
#     if request.method == 'POST':
#         data = {}
#         phone = request.data.get('phone', '0')
#         country_code = request.data.get('country_code', '0')
#         request_data = request.data.copy()
#         serializer = CreateElectricianSerializer(data=request_data)

#         request_data['password'] = request_data['password'] if 'password' in request_data else random_password(16)

#         if serializer.is_valid():
#             status_code = status.HTTP_200_OK
#             if(validate_phone(country_code,phone) and (not "username" in fetch_user_by_phone(phone))):
#                 # data = serializer.data
#                 data['status'] = 'success'
#                 data['message'] = 'User registration successful. OTP sent to the provided phone number.'
#                 otp = randint(1000, 9999)
#                 my_session = SessionStore()
#                 my_session['phone'] = phone
#                 my_session['country_code'] = country_code
#                 my_session['email'] = request_data['email'] if 'email' in request_data else None
#                 my_session['full_name'] = request_data['full_name'] if 'full_name' in request_data else None
#                 my_session['password'] = request_data['password']
#                 my_session['otp'] = otp
#                 my_session['otp_count'] = 5
#                 my_session.create()
#                 data['session_key'] = my_session.session_key
#                 send_phone_otp(country_code,phone,otp)
#                 my_session.save()
#             else:
#                 data['status'] = 'error'
#                 data['message'] = 'phone number already exists !'
#                 status_code = status.HTTP_400_BAD_REQUEST
#         else:
#             data['status'] = 'error'
#             data['message'] = 'User registration failed.'
#             data['errors'] = serializer.errors
#         return Response(data, status=status_code)
#     else:
#         return Response({""}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes((AllowAny, ))
# @parser_classes([JSONParser,FormParser, MultiPartParser,FileUploadParser])
# def electrician_verify_phone(request):
#     session_key = request.data.get('session_key')
#     my_session = SessionStore(session_key=session_key)
#     data = {}
#     otp = int(request.data.get('otp'))
#     if("otp" in my_session and "otp_count" in my_session) and otp == my_session['otp']  and (my_session['otp_count'] > 0):
#         request_data = request.data.copy()
#         request_data['country_code'] = my_session['country_code']
#         request_data['username'] = my_session['phone']
#         request_data['phone'] = my_session['phone']
#         request_data['email'] = my_session['email']
#         request_data['password'] = my_session['password']
#         fetch_data = register_user_by_phone(request_data)
#         serializer = CreateElectricianSerializer(data=request_data)
#         if serializer.is_valid() and "token" in fetch_data:
#             user = serializer.save()
#             user.phone_verified=True
#             user.save()
#             data['response'] = 'successfully registered new user.'
#             data['email'] = user.email
#             data['full_name'] = user.full_name
#             data['phone'] = user.phone
#             data['username'] = user.username
#             data['pk'] = user.pk
#             token = set_user_token(user,fetch_data["token"])
#             data['token'] = token
#             save_login_history(request,user,"registered with phone")
#             my_session.delete()    
#             status_code=status.HTTP_200_OK
#         else:
#             data = serializer.errors
#             status_code=status.HTTP_400_BAD_REQUEST
#     else:
#         if("otp_count" in my_session and my_session['otp_count'] > 0):
#             my_session['otp_count'] -= 1
#             data['error_message'] = "invalid OTP"
#         else:
#             my_session.delete()
#             data['error_message'] = "Limit Exceeded, Register again"

#         status_code=status.HTTP_400_BAD_REQUEST
#     return Response(data,status=status_code)

class ElectricianViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = Electrician.objects.all()
    serializer_class = CreateElectricianSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__full_name']

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewElectricianSerializer
        return CreateElectricianSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        User.objects.filter(pk=user.pk).delete()
        # user.delete()
        instance.delete()
        return Response({"message": "Electrician Deleted Successfully"}, status=status.HTTP_200_OK)
    
class ElectricianStaffViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = ElectricianStaff.objects.all()
    serializer_class = CreateElectricianStaffsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__full_name']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListViewElectricianStaffSerializer
        return CreateElectricianStaffsSerializer
    
    
class ElectricianPointTrackViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated ]
    queryset = ElectricianPointTrack.objects.all()
    serializer_class = ElectricianPointTrackSerializer
    filter_backends = [SearchFilter]
    search_fields = ['electrician__user__full_name']