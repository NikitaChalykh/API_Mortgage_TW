from rest_framework import viewsets

from mortgage.models import MortgageOffer

from .filters import OfferFilterBackend
from .serializers import ListOfferSerializer, OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = MortgageOffer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = (OfferFilterBackend,)
    ordering_fields = ('payment', 'rate')

    def get_serializer_class(self):
        if self.action == 'list':
            return ListOfferSerializer
        return OfferSerializer
