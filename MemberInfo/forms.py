from django import forms
from .models import MemberInfo

class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['name', 'goal', 'sex', 'age', 'height', 'weight', 'weight_goal', 'activity_level']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MemberInfoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(MemberInfoForm, self).save(commit=False)
        instance.member = self.user
        if commit:
            instance.save()
        return instance