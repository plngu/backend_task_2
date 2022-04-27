from api.views import OfferViewSet
from django.urls import path

app_name = 'offer'

urlpatterns = [
    path('offer/', OfferViewSet.as_view()),
    path('offer/<int:pk>/', OfferViewSet.as_view()),
]
