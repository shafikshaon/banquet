from django import forms

from accounts.models import SystemUser
from meals.models.meal import Meal

BREAKFAST_MEAL_COUNT = (
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
)

LUNCH_DINNER_MEAL_COUNT = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class MealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['member'] = forms.ModelChoiceField(
            queryset=SystemUser.objects.filter(is_delete=False, is_active=True),
            widget=forms.Select(
                attrs={
                    'class': 'form-control emphasized'
                }
            ),
            initial=self.instance.member if self.instance and self.instance.pk else None
        )
        self.fields['meal_date'] = forms.CharField(
            label='Meal for',
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control emphasized'
                }
            ),
            initial=self.instance.meal_date if self.instance and self.instance.pk else None
        )
        self.fields['breakfast'] = forms.ChoiceField(
            choices=BREAKFAST_MEAL_COUNT,
            widget=forms.Select(
                attrs={
                    'class': 'form-control emphasized'
                }
            ),
            initial=self.instance.breakfast if self.instance and self.instance.pk else 0.5
        )
        self.fields['lunch'] = forms.ChoiceField(
            choices=LUNCH_DINNER_MEAL_COUNT,
            widget=forms.Select(
                attrs={
                    'class': 'form-control emphasized'
                }
            ),
            initial=self.instance.lunch if self.instance and self.instance.pk else 1
        )
        self.fields['dinner'] = forms.ChoiceField(
            choices=LUNCH_DINNER_MEAL_COUNT,
            widget=forms.Select(
                attrs={
                    'class': 'form-control emphasized'
                }
            ),
            initial=self.instance.dinner if self.instance and self.instance.pk else 1
        )

    class Meta:
        model = Meal
        fields = ('member', 'meal_date', 'breakfast', 'lunch', 'dinner')
