from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import ValidateUsername


class UserRole(models.TextChoices):
    """Роли пользователей."""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True,
                                validators=[ValidateUsername()])
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    role = models.CharField(
        max_length=10,
        help_text='роль пользователя в системе',
        choices=UserRole.choices,
        default=UserRole.USER
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
