from django.utils import timezone

from django.conf import settings
from django.db import models


# Create your models here.
from common import enums
from common.models import Status


class Plan(models.Model):
    plan_name = models.CharField(max_length=200, null=True, blank=True)
    plan_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.plan_name


class UserApp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)
    app_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, default=enums.ACTIVE, null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name


class Subscription(models.Model):
    plan = models.ForeignKey(Plan, default=enums.FREE_PLAN, null=True, blank=True, on_delete=models.PROTECT)
    app = models.ForeignKey(UserApp, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.app.app_name + " " + self.plan.plan_name

