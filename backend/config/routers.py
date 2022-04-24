from rest_framework.routers import DefaultRouter

from rest_framework import routers
from django.urls import include, path
from rest_framework.authtoken import views

from api.views import OfferViewSet

router = routers.DefaultRouter()
router.register('offer', OfferViewSet, basename='offer')


urlpatterns = [
    path('', include(router.urls))
]
