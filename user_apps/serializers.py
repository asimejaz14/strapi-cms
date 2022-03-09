
from rest_framework import serializers

from user_apps.models import UserApp, Subscription


class UserAppSerializer(serializers.ModelSerializer):

    subscription = serializers.SerializerMethodField()
    subscription_status = serializers.SerializerMethodField()

    def get_subscription(self, obj):
        try:
            return Subscription.objects.filter(app=obj).first().plan.plan_name
        except:
            return None

    def get_subscription_status(self, obj):
        try:
            sub = Subscription.objects.filter(app=obj).first().status
            if sub is True:
                return "Active"
            return "Canceled"
        except:
            return None


    class Meta:
        model = UserApp
        fields = "__all__"

