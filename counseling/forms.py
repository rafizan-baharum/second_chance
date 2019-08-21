from django import forms

from .models import Session


class SessionModelForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['student', 'counselor', 'venue', 'remarks', 'counseled_date']
        widgets = {
            'counseled_date': forms.DateInput(attrs={'type': 'date'}),
        }
