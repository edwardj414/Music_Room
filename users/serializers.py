import re

from django.contrib.auth.hashers import make_password

from .models import *
from rest_framework import serializers


class CheckPassword:
    @staticmethod
    def validate_pass(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
        return bool(re.match(pattern, password))

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CusUser
        fields = ('username', 'email', 'password', 'first_name','last_name', 'phone_number')

    def validate_password(self, value):
        if not CheckPassword.validate_pass(value):
            raise serializers.ValidationError(
                "Password must contain upper, lower, number and special character"
            )
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CusUser.objects.create(**validated_data)
        return user