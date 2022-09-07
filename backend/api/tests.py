from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from mortgage.models import MortgageOffer


class ApiViewsTests(TestCase):
    """Создаем тестовую модель ипотечного предложения и
    тестовую модель пользователя."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.offer = MortgageOffer.objects.create(
            bank_name='alpha',
            term_min=20,
            term_max=30,
            rate_min=2.5,
            rate_max=6.7,
            payment_min=1000000,
            payment_max=10000000
        )

    def setUp(self):
        """Создаем клиент гостя."""
        self.guest_client = APIClient()

    def test_create_product(self):
        """Post запрос создает запись в модели."""
        offer_count = MortgageOffer.objects.count()
        data = {
            'bank_name': 'sberra',
            'term_min': 30,
            'term_max': 40,
            'rate_min': 3.5,
            'rate_max': 9.7,
            'payment_min': 2000000,
            'payment_max': 20000000
        }
        response = self.guest_client.post(
            reverse(
                'mortgageoffer-list'
            ),
            data=data,
            format='json'
        )
        new_offer = MortgageOffer.objects.last()
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(MortgageOffer.objects.count(), offer_count + 1)
        self.assertEqual(new_offer.bank_name, data['bank_name'])

    def test_delete_product(self):
        """Delete запрос удаляет запись из модели."""
        offer_count = MortgageOffer.objects.count()
        response = self.guest_client.delete(
            reverse(
                'mortgageoffer-detail',
                kwargs={'pk': ApiViewsTests.offer.id}
            ),
            format='json'
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(MortgageOffer.objects.count(), offer_count - 1)
