from django import forms

from .models import DemoRequest


class DemoRequestForm(forms.ModelForm):

    class Meta:

        model = DemoRequest

        fields = [
            "name",
            "institution_name",
            "email",
            "mobile",
            "institution_type",
            "student_strength",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Name"
                }
            ),

            "institution_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Institution Name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mobile Number"
                }
            ),

            "institution_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "student_strength": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Number of Students"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your requirements"
                }
            ),

        }

