from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK

from common.helpers import get_default_query_param
from language.response_utils import create_message
from user_apps.models import UserApp, Subscription
from user_apps.serializers import UserAppSerializer


class UserAppsController:

    @classmethod
    def get_app(cls, request, id=None):
        try:
            kwargs = {}
            if id:
                kwargs['id'] = id

            order = get_default_query_param(request, 'order', 'desc')
            order_by = get_default_query_param(request, 'order_by', 'created_at')
            limit = get_default_query_param(request, 'limit', None)
            offset = get_default_query_param(request, 'offset', None)
            kwargs['user_id'] = request.user.id

            if order == "asc":
                sort = order_by
            else:
                sort = "-" + order_by

            user_apps = UserApp.objects.filter(**kwargs).order_by(sort)
            if limit and offset:
                pagination = LimitOffsetPagination()
                user_apps = pagination.paginate_queryset(user_apps, request)
            serialized_apps = UserAppSerializer(user_apps, many=True)
            return Response(create_message([serialized_apps.data], 1000), HTTP_200_OK)


        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_app(cls, request):
        try:

            payload = request.data.copy()
            payload['user'] = request.user.id
            serialized_app = UserAppSerializer(data=payload)
            if serialized_app.is_valid():
                app = serialized_app.save()

                # create subscription of app with free plan
                Subscription.objects.create(app=app)
                return Response(create_message([serialized_app.data], 1000), HTTP_201_CREATED)
            else:
                return Response(create_message([serialized_app.errors], 1001), HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)


    def updated_app(self, request, id=None):
        ...

    def delete_app(self, request, id=None):
        try:
            if not id:
                return Response(create_message([], 1007), HTTP_200_OK)
            Subscription.objects.filter(app__user=request.user, app_id=id).update(status=False)
            return Response(create_message([], 1000), HTTP_200_OK)
        except Exception as e:
            return Response(create_message([e], 1002), HTTP_500_INTERNAL_SERVER_ERROR)