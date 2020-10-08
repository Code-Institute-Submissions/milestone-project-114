from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    name = models.CharField(max_length=254)
    monthly_price = models.DecimalField(max_digits=6, decimal_places=2)
    yearly_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    frequency = models.CharField(max_length=254)
    paid = models.CharField(max_length=254)
    incentive1 = models.CharField(max_length=254, null=True, blank=True)
    incentive2 = models.CharField(max_length=254, null=True, blank=True)
    incentive3 = models.CharField(max_length=254, null=True, blank=True)
    incentive4 = models.CharField(max_length=254, null=True, blank=True)
    incentive5 = models.CharField(max_length=254, null=True, blank=True)
    incentive6 = models.CharField(max_length=254, null=True, blank=True)
    incentive7 = models.CharField(max_length=254, null=True, blank=True)
    incentive8 = models.CharField(max_length=254, null=True, blank=True)
    incentive9 = models.CharField(max_length=254, null=True, blank=True)
    incentive10 = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class StripeCustomer(User):
    customer = models.ForeignKey('djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey('djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL)
