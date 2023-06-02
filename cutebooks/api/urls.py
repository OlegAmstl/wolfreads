from django.urls import path, include
from rest_framework import routers
from .views import IndexViewSet, BookViewSet, ChallengeViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('main', IndexViewSet, basename='index')
router_v1.register('books', BookViewSet, basename='books')
router_v1.register('challenge', ChallengeViewSet, basename='challenge')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
