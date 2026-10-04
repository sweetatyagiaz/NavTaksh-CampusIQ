from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DemoRequestForm


def demo_request(request):

    if request.method == "POST":

        form = DemoRequestForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you! Our team will contact you shortly."
            )

            return redirect(
                "contact:demo_request"
            )

    else:

        form = DemoRequestForm()

    context = {
        "form": form
    }

    return render(
        request,
        "contact/contact.html",
        context
    )