from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from kitchen.models import Cook


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "years_of_experience",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]

        if years_of_experience > 60:
            raise ValidationError(
                "Value must be less than or equal to 60"
            )
        return years_of_experience



