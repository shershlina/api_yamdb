from rest_framework import serializers

from .models import User, UserRole
from .validators import validate_username


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True,
                                     validators=[validate_username])

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate(self, data):
        username = User.objects.filter(username=data['username']).exists()
        email = User.objects.filter(email=data['email']).exists()
        if email and not username:
            raise serializers.ValidationError('400')
        if username and not email:
            raise serializers.ValidationError('400')
        return data


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


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)
