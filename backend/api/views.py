from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from offer.models import Offer
from .mixins import CreateUpdateDestroyMixin
from .serializers import OfferSerializer, calculate_mortgage


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('bank_name', 'term_min', 'term_max', 'rate_min',
                        'rate_max', 'payment_min', 'payment_max', )
    ordering_fields = ('bank_name', 'term_min', 'term_max', 'rate_min',
                       'rate_max', 'payment_min', 'payment_max', )

    # ?deposit=1000000&term=25&price=10000000
    def get_queryset(self):
        deposit = self.request.GET.get('deposit', None)
        term = self.request.GET.get('term', None)
        price = self.request.GET.get('price', None)
        client_request_list = [deposit, term, price]

        if all(client_request_list):
            # print(self.request.GET)
            price_min = price
            price_max = price
            # if 'payment_min' in self.request.GET:
            #     price_min = self.request.GET.get('payment_min')
            # if 'payment_max' in self.request.GET:
            #     price_max = self.request.GET.get('payment_max')
            queryset = Offer.objects.filter(
                term_min__lte=term,
                term_max__gte=term,
                payment_min__lte=price_min,
                payment_max__gte=price_max,
            )
            return queryset

        return Offer.objects.all()
