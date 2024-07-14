from rest_framework import serializers

from .models import IPAddress


class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'

