from django import forms

from .models import Food, WeekPlan


class FoodUpdateForm(forms.ModelForm):
    add_to_week_plan = forms.ModelMultipleChoiceField(
        queryset=WeekPlan.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Food
        fields = [
            "like",
            "is_allergic",
            "is_gluten_free",
            "add_to_week_plan",
        ]
   