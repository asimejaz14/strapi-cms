from django.db.models.signals import post_save
from django.dispatch import receiver

from user_apps.models import UserApp, Subscription


@receiver(post_save, sender=UserApp)
def associate_subscription_plan(sender, instance, created, **kwargs):
    if created:
        print("SIGNAL GENERATED")
        # create subscription of app with free plan
        Subscription.objects.create(app=instance)
