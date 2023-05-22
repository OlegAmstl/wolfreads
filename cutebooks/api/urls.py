from django.urls import path, include
from rest_framework import routers
from .views import IndexViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('main', IndexViewSet, basename='index')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
