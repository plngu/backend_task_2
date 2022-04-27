from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from offer.models import Offer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OfferSerializer


class OfferViewSet(APIView):
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('bank_name', 'term_min', 'term_max', 'rate_min',
                        'rate_max', 'payment_min', 'payment_max', )

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        deposit = self.request.query_params.get('deposit', None)
        term = self.request.query_params.get('term', None)
        price = self.request.query_params.get('price', None)

        payment_max = self.request.query_params.get('payment_max', None)
        payment_min = self.request.query_params.get('payment_min', None)

        client_request_list = [deposit, term, price]
        check_payment_borders = [payment_max, payment_min]

        if all(client_request_list):
            offer = Offer.objects.filter(
                term_min__lte=term,
                term_max__gte=term,
                payment_min__lte=price,
                payment_max__gte=price,
            )
            serializer = OfferSerializer(
                offer,
                many=True,
                context={'request': request}
            )

            if any(check_payment_borders):
                serializer_data = []
                payment_min = int(payment_min)
                payment_max = int(payment_max)
                if payment_max and payment_min:
                    for elem in serializer.data:
                        if payment_min <= elem['payment'] <= payment_max:
                            serializer_data.append(elem)
                    return Response(serializer_data)

                if payment_max and not payment_min:
                    for elem in serializer.data:
                        if elem['payment'] <= payment_max:
                            serializer_data.append(elem)
                    return Response(serializer_data)

                if payment_min and not payment_max:
                    for elem in serializer.data:
                        if payment_min <= elem['payment']:
                            serializer_data.append(elem)
                    return Response(serializer_data)
            else:
                serializer = OfferSerializer(
                    offer,
                    many=True,
                    context={'request': request}
                )
                return Response(serializer.data)

        offer = Offer.objects.all()
        filtered_offers = self.filter_queryset(offer)
        serializer = OfferSerializer(
            filtered_offers,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = OfferSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(
            offer,
            data=request.data,
            context={'request': request},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
