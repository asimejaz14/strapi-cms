from django.urls import path

from user.views import (UserLoginAPIView, UserSignUp, UserLogoutAPIView, UserPasswordResetAPIView)

urlpatterns = [
    path("signup", UserSignUp.as_view(), name="signup"),
    path("login", UserLoginAPIView.as_view(), name="login"),
    path("logout", UserLogoutAPIView.as_view(), name="logout"),
    path("reset-password", UserPasswordResetAPIView.as_view(), name="reset password"),
]
