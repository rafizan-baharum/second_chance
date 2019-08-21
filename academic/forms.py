from django import forms

from .models import Resultbook, Result


class ResultbookModelForm(forms.ModelForm):
    class Meta:
        model = Resultbook
        fields = ['student', 'semester', 'level', 'school']


class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['parent', 'subject', 'grade']
