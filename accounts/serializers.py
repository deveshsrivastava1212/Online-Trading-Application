from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    
# Register Serializer
class RegisterSerializer(serializers.ModelSerialzer):
    class Meta:
        model = User
        field = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validate_data['username'],validated_data['email'],
            validated_data['password']
        )
        return user
    
#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidateError("Incorrect Credentials")
    
# Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoints.
    """
    old_password = serializers.CharField(requied = True)
    new_password = serializers.CharField(required = True)

    def validate_new_password(self,value):
        validate_password(value)
        return value