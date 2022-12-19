
from rest_framework import serializers

from .models import User, UserRole


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(default=UserRole.USER, choices=UserRole)

    class Meta:
        model = User
        exclude = ('id', 'password', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined',
                   'groups', 'user_permissions')
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
