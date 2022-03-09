from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from user.user_controller import UserSignUpController, UserLoginController, UserLogoutController, \
    PasswordResetController


class UserSignUp(APIView):
    permission_classes = [AllowAny]
    user_signup = UserSignUpController()

    def post(self, request):
        return self.user_signup.user_signup(request)


class UserLoginAPIView(APIView):
    user_login_controller = UserLoginController()
    permission_classes = [AllowAny]

    def post(self, request):
        return self.user_login_controller.login_user(request)


class UserLogoutAPIView(APIView):
    user_logout_controller = UserLogoutController()
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return self.user_logout_controller.logout_user(request)


class UserPasswordResetAPIView(APIView):
    password_reset_controller = PasswordResetController()
    permission_classes = [AllowAny]

    def patch(self, request):
        return self.password_reset_controller.reset_password(request)