# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt


# import os


# @csrf_exempt
# def ip_view(req):
#     if req.method == 'POST':
#         print(req.POST)
#         ip = req.POST.get('ip')
#         # response = os.system(f"ping {param} 1 {hostname}")
#         response = os.popen(f"ping -c 2 {ip}").read()
#         return HttpResponse(f'success!\n {response}', status=200)

from django.core.exceptions import ValidationError


from rest_framework import viewsets, status
from rest_framework.response import Response


from .serializers import IPSerializer
from .models import IPAddress
from .exceptions import InvalidIPExeption


import os
import logging

logger = logging.getLogger(__name__)


class PingIPAddressViewSet(viewsets.ViewSet):
    serializer_class = IPSerializer

    def create(self, request):
        """
            payload for using this API is:
                {"ip":"192.168.1.1"}
        """
        client_ip = request.META.get('REMOTE_ADDR')
        print(f'client ip {client_ip}')
        try:
            ip_address = request.data.get('ip')
            ip_obj = IPAddress.objects.create(ip=ip_address)
            ping_output = os.popen(f"ping -c 4 {ip_obj.ip}").read()

            return Response({"message": ping_output}, status=status.HTTP_201_CREATED)

        except ValidationError:
            logging.warning(f"client ip {client_ip} input INVALID_IP_FORMAT")
            return Response({"message": "invalid IP Address"}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidIPExeption:
            logging.warning(f"client ip {client_ip} input BLACK_LIST_IP")
            return Response({"message": "invalid IP Address"}, status=status.HTTP_400_BAD_REQUEST)
