from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_201_CREATED, HTTP_200_OK

from language.response_utils import create_message
from user.models import User
from user.serializers import UserSerializer


class UserSignUpController:
    @classmethod
    def user_signup(cls, request):
        try:
            if User.objects.filter(email=request.data.get("email")).exists():
                return Response(create_message([], 1003), status=HTTP_409_CONFLICT)
            serialized_user = UserSerializer(data=request.data)
            if serialized_user.is_valid():
                serialized_user.save()

                return Response(
                    create_message([serialized_user.data], 1000),
                    status=HTTP_201_CREATED,
                )
            else:
                return Response(
                    create_message([serialized_user.errors], 1001),
                    status=HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            return Response(
                create_message([e], 1002), status=HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserLoginController:
    @classmethod
    def login_user(cls, request):
        try:
            email_ = request.data.get("email")
            password_ = request.data.get("password")

            user = authenticate(request, email=email_, password=password_)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    token_ = Token.objects.get(user=user)
                    response = {"token": str(token_)}
                    return Response(create_message(response, 1000), status=HTTP_200_OK)
                elif token:
                    response = {"token": str(token)}
                    return Response(create_message(response, 1000), status=HTTP_200_OK)
            else:
                return Response(create_message([], 1004), status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                create_message([e], 1002), status=HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserLogoutController:

    @classmethod
    def logout_user(cls, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()

            return Response(create_message([], 1000), status=HTTP_200_OK)

        except Exception as e:
            return Response(
                create_message([e], 1002), status=HTTP_500_INTERNAL_SERVER_ERROR
            )


class PasswordResetController:

    @classmethod
    def reset_password(cls, request):
        try:
            email = request.data.get("email")
            current_password = request.data.get("current_password")
            new_password = request.data.get("new_password")
            user = authenticate(request, email=email, password=current_password)

            if user:
                User.objects.filter(email=email).update(password=make_password(new_password))
                return Response(
                    create_message([], 1005), status=HTTP_200_OK
                )
            else:
                return Response(
                    create_message([], 1006), status=HTTP_200_OK
                )

        except Exception as e:
            return Response(
                create_message([e], 1002), status=HTTP_500_INTERNAL_SERVER_ERROR
            )