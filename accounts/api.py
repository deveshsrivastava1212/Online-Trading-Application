from rest_framework import generics, permissions, status
#import response to send response form this api
from rest_framework.response import response
#import auth token from knox authentication system
from knox.models import AuthToken
from django.contrib.auth.models import User


#Register API
class RegisterAPI(generics.GenericAPIView):
    