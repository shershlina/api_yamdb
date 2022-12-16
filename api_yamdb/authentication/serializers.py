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
        fields = ('username', 'role', 'bio', 'email', 'first_name', 'last_name',)
