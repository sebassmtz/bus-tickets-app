from django.db import models


class Business(models.Model):
    nit = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    withholding_tax = models.FloatField(max_length=10)
    business_code = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.name