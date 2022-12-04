from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=15, verbose_name='currency name')
    quote_usdt = models.FloatField()

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencys'

    def __str__(self):
        return self.name
