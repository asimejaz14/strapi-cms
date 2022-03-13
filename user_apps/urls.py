
from django.urls import path

from user_apps import views

urlpatterns = [
    path('', views.UserAppsAPIView.as_view()),
    path('<int:id>', views.UserAppsAPIView.as_view()),

    # subscription details
    path('subscription-details', views.SubscriptionAPIView.as_view()),
    path('update-subscription', views.SubscriptionAPIView.as_view()),
    path('cancel-subscription', views.SubscriptionAPIView.as_view()),

]
