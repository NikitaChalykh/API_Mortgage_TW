from rest_framework import serializers

from api.utils import mortgage_calculator
from mortgage.models import MortgageOffer


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = MortgageOffer
        fields = (
            'id', 'bank_name', 'term_min', 'term_max',
            'rate_min', 'rate_max', 'payment_min', 'payment_max'
        )


class ListOfferSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()

    class Meta:
        model = MortgageOffer
        fields = (
            'id', 'payment', 'rate', 'bank_name', 'term_min', 'term_max',
            'rate_min', 'rate_max', 'payment_min', 'payment_max'
        )

    def get_payment(self, obj):
        price = (
            self.context['request'].query_params.get('price')
        )
        deposit = (
            self.context['request'].query_params.get('deposit')
        )
        term = (
            self.context['request'].query_params.get('term')
        )
        if (price and deposit and term) is not None:
            return mortgage_calculator(obj, price, deposit, term)
        return None

    def get_rate(self, obj):
        price = (
            self.context['request'].query_params.get('price')
        )
        deposit = (
            self.context['request'].query_params.get('deposit')
        )
        if (price and deposit) is not None:
            return mortgage_calculator(obj, price, deposit)
        return None
