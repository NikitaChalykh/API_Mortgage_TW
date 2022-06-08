from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from mortgage.models import MortgageOffer

User = get_user_model()


class ApiURLTests(TestCase):
    """Создаем тестовую модель ипотченого
    предложения."""
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

    def test_urls_response_guest(self):
        """Проверяем статус страниц для гостя."""
        url_status = {
            reverse('mortgageoffer-list'): HTTPStatus.OK,
            reverse(
                'mortgageoffer-detail',
                kwargs={'pk': ApiURLTests.offer.id}
            ): HTTPStatus.OK
        }
        for url, status_code in url_status.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, status_code)
