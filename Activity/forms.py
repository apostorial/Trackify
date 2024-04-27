from django import forms

class ActivityForm(forms.Form):
    query = forms.CharField(max_length=255, required=True)
    duration = forms.FloatField(required=True)