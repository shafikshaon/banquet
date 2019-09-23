from django import forms
from django.forms import ModelForm

from accounts.models import SystemUser
from configuration.models import MealConfig


class MealConfigForm(ModelForm):
    breakfast = forms.DecimalField(
        label='Breakfast',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control emphasized',
                'autofocus': 'autofocus',
                'placeholder': 'Breakfast',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter breakfast'},
        required=True
    )

    lunch = forms.DecimalField(
        label='Lunch',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Lunch',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter lunch'},
        required=True
    )

    dinner = forms.DecimalField(
        label='Dinner',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Dinner',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter dinner'},
        required=True
    )

    class Meta:
        model = MealConfig
        fields = ("breakfast", "lunch", "dinner")

    def clean_breakfast(self):
        # password1 = self.cleaned_data.get("password1")
        # password2 = self.cleaned_data.get("password2")
        # if password1 and password2 and password1 != password2:
        #     raise forms.ValidationError(
        #         self.error_messages['password_mismatch'],
        #         code='password_mismatch',
        #     )
        return self.cleaned_data.get("breakfast")
