from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    DashboardRedirectView,
)

urlpatterns = [

    path(
        "login/",
        UserLoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        UserLogoutView.as_view(),
        name="logout"
    ),

    path(
        "dashboard/",
        DashboardRedirectView.as_view(),
        name="dashboard"
    ),
]