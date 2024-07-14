from django.test import TestCase


from rest_framework.test import APIRequestFactory
from rest_framework import status


from ..views import PingIPAddressViewSet
from ..models import IPAddress


class PingIPAddressViewSetTestCase(TestCase):
    def test_create_ping_ipaddress(self):
        factory = APIRequestFactory()
        ip_address = '192.168.1.1'
        request_data = {'ip': ip_address}
        request = factory.post('/ip/', request_data)

        view = PingIPAddressViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('PING' in response.data.get('message'))

        # Verify that an IPAddress object with the specified IP address was created
        ip_obj = IPAddress.objects.filter(ip=ip_address).exists()
        self.assertTrue(ip_obj)

    def test_create_invalid_ipaddress_localhost(self):
        factory = APIRequestFactory()
        ip_address = '127.0.0.1'
        request_data = {'ip': ip_address}
        request = factory.post('/ip/', request_data)

        view = PingIPAddressViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('invalid' in response.data.get('message'))
        ip_obj = IPAddress.objects.filter(ip=ip_address).exists()
        self.assertFalse(ip_obj)

    def test_create_invalid_ipaddress_base(self):
        factory = APIRequestFactory()
        ip_address = '0.0.0.0'
        request_data = {'ip': ip_address}
        request = factory.post('/ip/', request_data)

        view = PingIPAddressViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('invalid' in response.data.get('message'))
        ip_obj = IPAddress.objects.filter(ip=ip_address).exists()
        self.assertFalse(ip_obj)

    def test_create_invalid_ipaddress_invalidIpv4(self):
        factory = APIRequestFactory()
        ip_address = '129.1233.12.1'
        request_data = {'ip': ip_address}
        request = factory.post('/ip/', request_data)

        view = PingIPAddressViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('invalid' in response.data.get('message'))
        ip_obj = IPAddress.objects.filter(ip=ip_address).exists()
        self.assertFalse(ip_obj)

    def test_create_invalid_ipaddress_invalidIpv6(self):
        factory = APIRequestFactory()
        ip_address = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        request_data = {'ip': ip_address}
        request = factory.post('/ip/', request_data)

        view = PingIPAddressViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('invalid' in response.data.get('message'))

        ip_obj = IPAddress.objects.filter(ip=ip_address).exists()
        self.assertFalse(ip_obj)
