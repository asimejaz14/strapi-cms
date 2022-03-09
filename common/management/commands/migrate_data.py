from django.core.management import BaseCommand

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
            id=0, plan_name="Pro", plan_price=25
        )

        self.stdout.write(
            self.style.SUCCESS(f"Data migrations for '{TABLE_NAME}' ran successfully!")
        )

