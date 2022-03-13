
from rest_framework.views import APIView

from user_apps.controller import UserAppsController, SubscriptionController


class UserAppsAPIView(APIView):

    user_apps_controller = UserAppsController()

    @classmethod
    def get(cls, request):
        return cls.user_apps_controller.get_app(request)

    @classmethod
    def post(cls, request):
        return cls.user_apps_controller.create_app(request)

    @classmethod
    def patch(cls, request):
        return cls.user_apps_controller.updated_app(request)

    @classmethod
    def delete(cls, request, id=None):
        return cls.user_apps_controller.delete_app(request, id)


class SubscriptionAPIView(APIView):
    subscription_controller = SubscriptionController()

    @classmethod
    def get(cls, request):
        return cls.subscription_controller.get_subscription_of_app(request)

    def patch(cls, request):
        if request.path == "/user-apps/cancel-subscription":
            return cls.subscription_controller.cancel_subscription_of_app(request)
        else:
            return cls.subscription_controller.update_subscription_of_app(request)

