from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Pricing(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        signup_free = Pricing.objects.get(name='Signup Free')
        Subscription.objects.create(user=instance, pricing=signup_free)


post_save.connect(post_save_user, sender=User)
