from django import forms

class MealForm(forms.Form):
    query = forms.CharField(max_length=255, required=True)