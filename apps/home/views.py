from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, "home/index.html")

class PlatformDashboardView(
    LoginRequiredMixin,
    TemplateView
):
    template_name = "dashboard/platform_dashboard.html"


class SchoolDashboardView(
    LoginRequiredMixin,
    TemplateView
):
    template_name = "dashboard/school_dashboard.html"