from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_valid_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
