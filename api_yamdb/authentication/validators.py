import re

from django.core.exceptions import ValidationError

def ValidateUsername(value):
    pattern = re.compile(r'^[\w.@+-]+\Z')
    if value != 'me' and pattern.match(value):
        return value
    raise ValidationError(
        'username должно соответствовать паттерну по документации')
