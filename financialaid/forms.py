from django import forms

from .models import Grant


class GrantModelForm(forms.ModelForm):
    class Meta:
        model = Grant
        fields = ['donor', 'amount', 'purpose','student', 'remarks', 'approved_date', 'disbursed_date']
        widgets = {
            'approved_date': forms.DateInput(attrs={'type': 'date'}),
            'disbursed_date': forms.DateInput(attrs={'type': 'date'}),
        }
