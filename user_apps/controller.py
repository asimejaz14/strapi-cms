from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_403_FORBIDDEN

from common import enums
from common.helpers import get_default_query_param, verify_user_in_request
from language.response_utils import create_message
from user_apps.models import UserApp, Subscription
from user_apps.serializers import UserAppSerializer, SubscriptionSerializer


class UserAppsController:

    @classmethod
    def get_app(cls, request):
        try:
            kwargs = {}
            app_id = get_default_query_param(request, 'app_id', None)
            order = get_default_query_param(request, 'order', 'desc')
            order_by = get_default_query_param(request, 'order_by', 'created_at')
            limit = get_default_query_param(request, 'limit', None)
            offset = get_default_query_param(request, 'offset', None)
            kwargs['user_id'] = request.user.id
            kwargs['status_id'] = enums.ACTIVE

            if app_id:
                kwargs['id'] = app_id

            if order == "asc":
                sort = order_by
            else:
                sort = "-" + order_by

            user_apps = UserApp.objects.filter(**kwargs).order_by(sort)
            user_count = user_apps.count()
            if limit and offset:
                pagination = LimitOffsetPagination()
                user_apps = pagination.paginate_queryset(user_apps, request)
            serialized_apps = UserAppSerializer(user_apps, many=True)
            return Response(create_message({"count": user_count, "data": serialized_apps.data}, 1000), HTTP_200_OK)

        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_app(cls, request):
        try:

            payload = request.data.copy()
            payload['user'] = request.user.id
            serialized_app = UserAppSerializer(data=payload)
            if serialized_app.is_valid():
                serialized_app.save()

                # # create subscription of app with free plan
                # Subscription.objects.create(app=app)
                return Response(create_message(serialized_app.data, 1000), HTTP_201_CREATED)
            else:
                return Response(create_message(serialized_app.errors, 1001), HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def updated_app(cls, request):
        try:
            app_id = request.data.get("app_id")
            if not app_id:
                return Response(create_message([], 1008), HTTP_400_BAD_REQUEST)

            user_app = UserApp.objects.filter(id=app_id, user_id=request.user.id).first()

            serialized_user_app = UserAppSerializer(user_app, data=request.data, partial=True)
            if serialized_user_app.is_valid():
                serialized_user_app.save()
                return Response(create_message(serialized_user_app.data, 1013), HTTP_200_OK)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_app(cls, request, id=None):
        try:
            if not id:
                return Response(create_message([], 1007), HTTP_200_OK)
            UserApp.objects.filter(id=id).update(status=enums.DELETED)
            Subscription.objects.filter(app__user=request.user, app_id=id).update(status=False)
            return Response(create_message([], 1000), HTTP_200_OK)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionController:

    @classmethod
    def get_subscription_of_app(cls, request):
        try:

            app_id = get_default_query_param(request, "app_id", None)

            kwargs = {}
            if app_id:
                kwargs["app_id"] = app_id
            kwargs['app__user_id'] = request.user.id

            subscription_detail = Subscription.objects.filter(**kwargs).order_by('-created_at')

            serialized_subscription_detail = SubscriptionSerializer(subscription_detail, many=True)

            return Response(create_message(serialized_subscription_detail.data, 1000), HTTP_200_OK)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_subscription_of_app(cls, request):
        try:

            app_id = request.data.get("app_id")
            plan_id = request.data.get("plan_id")
            if not app_id:
                return Response(create_message([], 1008), HTTP_400_BAD_REQUEST)
            if not plan_id:
                return Response(create_message([], 1010), HTTP_400_BAD_REQUEST)

            subscription = Subscription.objects.filter(app_id=app_id).first()

            # check if the user requesting his own data or not
            if not verify_user_in_request(request, subscription):
                return Response(create_message([], 1009), HTTP_403_FORBIDDEN)

            subscription.app_id = app_id
            subscription.plan_id = plan_id
            subscription.save()

            serialized_subscription = SubscriptionSerializer(subscription)

            return Response(create_message([serialized_subscription.data], 1011), HTTP_200_OK)

        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def cancel_subscription_of_app(cls, request):
        try:
            app_id = request.data.get("app_id")
            if not app_id:
                return Response(create_message([], 1008), HTTP_400_BAD_REQUEST)

            Subscription.objects.filter(app_id=app_id).update(status=False)
            return Response(create_message([], 1012), HTTP_200_OK)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)
