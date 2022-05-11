from offer.models import Offer
from rest_framework import serializers

from .utils import calculate_mortgage


class OfferSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Offer
        fields = ('id', 'payment', 'bank_name', 'term_min', 'term_max',
                  'rate_min', 'rate_max', 'payment_min', 'payment_max')

    def get_payment(self, obj):
        deposit = self.context['request'].query_params.get('deposit', None)
        term = self.context['request'].query_params.get('term', None)
        price = self.context['request'].query_params.get('price', None)
        client_request_list = [deposit, term, price]

        if not all(client_request_list):
            return ('Выберите начальный взнос, '
                    'срок ипотеки и цену недвижимости')

        [deposit, term, price] = [*map(int, client_request_list)]

        if deposit >= price:
            raise serializers.ValidationError(
                'Первый взнос не может быть больше или равен сумме кредита')

        percent = obj.rate_min
        return calculate_mortgage(deposit, term, price, percent)
