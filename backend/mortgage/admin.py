from django.contrib import admin

from .models import MortgageOffer


class MortgageOfferAdmin(admin.ModelAdmin):
    list_display = (
        'bank_name',
        'term_min',
        'term_max',
        'rate_min',
        'rate_max',
        'payment_min',
        'payment_max'
    )
    list_filter = ('bank_name',)
    empty_value_display = '-пусто-'


admin.site.register(MortgageOffer, MortgageOfferAdmin)
