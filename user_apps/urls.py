
from django.urls import path

from user_apps import views

urlpatterns = [
    path('', views.UserAppsAPIView.as_view()),
    path('<int:id>', views.UserAppsAPIView.as_view()),
]
