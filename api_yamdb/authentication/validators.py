from rest_framework import serializers
import re
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateUsername(object):
    def __call__(self, value: str):
        pattern = re.compile(r"^[\w.@+-]+\Z")
        if value != 'me' and pattern.match(value):
            return value
        raise serializers.ValidationError(
            'username должно соответствовать паттерну по документации')
