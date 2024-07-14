from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address

from .exceptions import InvalidIPExeption


def validate_ip_address(value):
    try:
        validate_ipv4_address(value)
    except ValidationError:
        raise ValidationError(
            '%(value)s is not a valid IP address', params={'value': value})


IP_BLACK_LIST = ['127.0.0.1', '0.0.0.0',]


class IPAddress(models.Model):
    ip = models. GenericIPAddressField()

    def save(self, *args, **kwargs):
        try:
            validate_ipv4_address(self.ip)

            if self.ip in IP_BLACK_LIST:
                raise InvalidIPExeption("ip exists in black list.")
            super(IPAddress, self).save(*args, **kwargs)

        except ValidationError:
            raise ValidationError(
                '%(value)s is not a valid IP address', params={'value': self.ip})

    def __str__(self) -> str:
        return self.ip
