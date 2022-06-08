from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MortgageOffer(models.Model):
    bank_name = models.CharField(
        verbose_name='Наименование банка',
        max_length=10
    )
    term_min = models.PositiveIntegerField(
        verbose_name='Срок ипотеки, ОТ'
    )
    term_max = models.PositiveIntegerField(
        verbose_name='Срок ипотеки, ДО'
    )
    rate_min = models.FloatField(
        verbose_name='Ставка, ОТ'
    )
    rate_max = models.FloatField(
        verbose_name='Ставка, ДО'
    )
    payment_min = models.PositiveIntegerField(
        verbose_name='Сумма кредита, ОТ'
    )
    payment_max = models.PositiveIntegerField(
        verbose_name='Сумма кредита, ДО'
    )

    class Meta:
        verbose_name = "Ипотечное предложение"
        verbose_name_plural = "Ипотечные предложения"

    def __str__(self):
        return self.bank_name
