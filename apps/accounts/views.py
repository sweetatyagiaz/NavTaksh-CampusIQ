from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView

from .forms import LoginForm


class UserLoginView(LoginView):

    template_name = "accounts/login.html"

    authentication_form = LoginForm

    redirect_authenticated_user = True


class UserLogoutView(LogoutView):

    next_page = "home"


class DashboardRedirectView(
    LoginRequiredMixin,
    RedirectView
):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        user = self.request.user

        if user.is_platform_admin:
            return "/dashboard/platform/"

        return "/dashboard/school/"