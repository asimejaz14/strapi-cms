
from rest_framework.views import APIView

from user_apps.user_app_controller import UserAppsController


class UserAppsAPIView(APIView):

    user_apps_controller = UserAppsController()

    @classmethod
    def get(cls, request, id=None):
        return cls.user_apps_controller.get_app(request, id)

    @classmethod
    def post(cls, request):
        return cls.user_apps_controller.create_app(request)

    @classmethod
    def patch(cls, request, id=None):
        return cls.user_apps_controller.updated_app(request, id)

    @classmethod
    def delete(cls, request, id=None):
        return cls.user_apps_controller.delete_app(request, id)