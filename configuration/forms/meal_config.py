from django import forms
from django.forms import ModelForm

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
        error_messages={'required': 'Please enter breakfast unit'},
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
        error_messages={'required': 'Please enter lunch unit'},
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
        error_messages={'required': 'Please enter dinner unit'},
        required=True
    )

    class Meta:
        model = MealConfig
        fields = ("breakfast", "lunch", "dinner")

    def clean_breakfast(self):
        breakfast = self.cleaned_data.get("breakfast")
        if breakfast and breakfast <= 0:
            raise forms.ValidationError(
                message='Breakfast unit should be more than 0'
            )
        return breakfast

    def clean_lunch(self):
        lunch = self.cleaned_data.get("lunch")
        if lunch and lunch <= 0:
            raise forms.ValidationError(
                message='Lunch unit should be more than 0'
            )
        return lunch

    def clean_dinner(self):
        dinner = self.cleaned_data.get("dinner")
        if dinner and dinner <= 0:
            raise forms.ValidationError(
                message='Dinner unit should be more than 0'
            )
        return dinner
