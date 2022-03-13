from django.core.management import BaseCommand

from common.models import Status
from user_apps.models import Plan


class Command(BaseCommand):
    help = "Data Migrations For Subscription Plans"

    def handle(self, *args, **kwargs):
        """Data migrations for Common Statuses"""
        TABLE_NAME = "Plan"
        record = Plan.objects.get_or_create(
            id=1, plan_name="Free", plan_price=0
        )
        record = Plan.objects.get_or_create(
            id=2, plan_name="Standard", plan_price=10
        )
        record = Plan.objects.get_or_create(
            id=3, plan_name="Pro", plan_price=25
        )


        self.stdout.write(
            self.style.SUCCESS(f"Data migrations for '{TABLE_NAME}' ran successfully!")
        )

        TABLE_NAME = "Status"
        record = Status.objects.get_or_create(
            id=1, name="Active", code="A", description="Record is active"
        )
        record = Status.objects.get_or_create(
            id=2, name="Deleted", code="D", description="Record is deleted"
        )
        self.stdout.write(
            self.style.SUCCESS(f"Data migrations for '{TABLE_NAME}' ran successfully!")
        )
