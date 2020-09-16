from django.db import models



class RateList(models.Model):
    flat_currency = models.CharField(max_length=3)
    variable_currency = models.CharField(max_length=3)
    rate = models.FloatField()


    class Meta:
        verbose_name = "RateList"
        verbose_name_plural = "RateLists"

    def __str__(self):
        return '{flat} to {var}'.format(flat=self.flat_currency,var=self.variable_currency)


    
