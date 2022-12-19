
from rest_framework import serializers

from .models import User, UserRole


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default=UserRole.USER)

    class Meta:
        model = User
        exclude = ('id', 'password', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined',
                   'groups', 'user_permissions')
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def validate_role(self, value):
        if self.context['request'].path == '/api/v1/users/me/':
            return self.instance.role
        if value not in UserRole:
            raise serializers.ValidationError(
                'передана несуществующая роль')
        return value
