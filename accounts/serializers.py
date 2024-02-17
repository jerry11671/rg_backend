from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.hashers import make_password
# import bcrypt

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'full_name', 'password', 'profile_pic']

    def validate_password(self, value):
        validate_password(value)
        return value  
    
    def create(self, validated_data):
        password = self.validated_data['password']
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
        
