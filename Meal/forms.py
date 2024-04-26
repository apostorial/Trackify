from django import forms

class MealForm(forms.Form):
    date = forms.DateField(label='Date')
    query = forms.CharField(max_length=255, required=True)