from django.db.models import Q
from rest_framework import filters

from api.utils import mortgage_calculator


class OfferFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        rate_min = request.query_params.get('rate_min')
        rate_max = request.query_params.get('rate_max')
        payment_min = request.query_params.get('payment_min')
        payment_max = request.query_params.get('payment_max')
        price = request.query_params.get('price')
        term = request.query_params.get('term')
        deposit = request.query_params.get('deposit')
        order = request.query_params.get('order')
        new_queryset = queryset
        if rate_min is not None:
            new_queryset = new_queryset.filter(
                rate_min__lte=int(rate_min)
            )
        if rate_max is not None:
            new_queryset = new_queryset.filter(
                rate_max__gte=int(rate_max)
            )
        if payment_min is not None:
            new_queryset = new_queryset.filter(
                payment_min__lte=payment_min
            )
        if payment_max is not None:
            new_queryset = new_queryset.filter(
                payment_max__gte=payment_max
            )
        if term is not None:
            new_queryset = new_queryset.filter(
                Q(term_min__lte=int(term))
                & Q(term_max__gte=int(term))
            )
        if price is not None:
            new_queryset = new_queryset.filter(
                Q(payment_min__lte=int(price))
                & Q(payment_max__gte=int(price))
            )
        if (price and deposit and term and order) is not None:
            if order == 'rate':
                new_queryset = sorted(
                    new_queryset,
                    key=lambda x: mortgage_calculator(x, price, deposit)
                )
            if order == '-rate':
                new_queryset = sorted(
                    new_queryset,
                    key=lambda x: mortgage_calculator(x, price, deposit),
                    reverse=True
                )
            if order == 'payment':
                new_queryset = sorted(
                    new_queryset,
                    key=lambda x: mortgage_calculator(x, price, deposit, term)
                )
            if order == '-payment':
                new_queryset = sorted(
                    new_queryset,
                    key=lambda x: mortgage_calculator(x, price, deposit, term),
                    reverse=True
                )
        return new_queryset
