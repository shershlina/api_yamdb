from rest_framework import serializers

from .models import User, UserRole
import re


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        pattern = re.compile(r"^[\w.@+-]+\Z")
        if pattern.match(value):
            return value
        raise serializers.ValidationError(
                "username должно соответствовать паттерну по документации")


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default=UserRole.USER)

    class Meta:
        model = User
        fields = ('username', 'role', 'bio', 'email',
                  'first_name', 'last_name',)
    
    def validate_username(self, value):
        pattern = re.compile(r"^[\w.@+-]+\Z")
        if pattern.match(value):
            return value
        raise serializers.ValidationError(
                "username должно соответствовать паттерну по документации")
