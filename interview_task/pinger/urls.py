from django.urls import path, include

from rest_framework.routers import DefaultRouter


from .views import PingIPAddressViewSet


router = DefaultRouter()
router.register(r'ip', PingIPAddressViewSet, basename='ip')

urlpatterns = [
    path('', include(router.urls)),
]
