from django.db import models

# Create your models here.

class GDP_IN_US_dollar(models.Model):
    year = models.IntegerField()
    gdp_usd = models.FloatField()

    def __str__(self):
        return str(self.year)