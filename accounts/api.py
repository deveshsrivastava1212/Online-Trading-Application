from requests import Response
from rest_framework import generics, permissions, status
#import response to send response form this api
from rest_framework.response import response
#import auth token from knox authentication system
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ChangePasswordSerializer
from django.contrib.auth.models import User


#Register API
class RegisterAPI(generics.GenericAPIView):
    serialzer_class = RegisterSerializer

    #email, password etc will be sent from here
    def post(self, request, *args, **kwargs):
        #data come in request will pass into serializer
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "bearer" : AuthToken.objects.create(user)[1]
        })
    
#Login API
class LoginAPI(generics.GenericAPIView):
    serialzer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validare_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "bearer": AuthToken.objects.create(user)[1]
        })