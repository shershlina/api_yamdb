import re

from rest_framework import serializers

from .models import User, UserRole


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        pattern = re.compile(r'^[\w.@+-]+\Z')
        if pattern.match(value) and value != 'me':
            return value
        raise serializers.ValidationError(
            'username должно соответствовать паттерну по документации')


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default=UserRole.USER)

    class Meta:
        model = User
        fields = ('username', 'role', 'bio', 'email',
                  'first_name', 'last_name',)
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def validate_username(self, value):
        pattern = re.compile(r"^[\w.@+-]+\Z")
        if pattern.match(value) and value != 'me':
            return value
        raise serializers.ValidationError(
            'username должно соответствовать паттерну по документации')

    def validate_role(self, value):
        if self.context['request'].path == '/api/v1/users/me/':
            return self.instance.role
        if value not in UserRole:
            raise serializers.ValidationError(
                'передана несуществующая роль')
        return value
