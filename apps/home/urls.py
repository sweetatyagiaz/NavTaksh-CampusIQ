from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),

    path(
        "dashboard/platform/",
        views.PlatformDashboardView.as_view(),
        name="platform_dashboard"
    ),

    path(
        "dashboard/school/",
        views.SchoolDashboardView.as_view(),
        name="school_dashboard"
    ),
]