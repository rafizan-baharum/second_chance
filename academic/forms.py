from django import forms

from portfolio.models import School
from .models import Resultbook, Result, Semester, Subject, Level


class SemesterModelForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['code', 'name']

    def clean_code(self, *args, **kwargs):
        instance = self.instance
        code = self.cleaned_data.get('code')
        qs = Semester.objects.filter(code__iexact=code)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This semester has already been registered. Please try again.")
        return code


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name']

    def clean_code(self, *args, **kwargs):
        instance = self.instance
        code = self.cleaned_data.get('code')
        qs = Subject.objects.filter(code__iexact=code)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This subject has already been registered. Please try again.")
        return code


class LevelModelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['code', 'name']

    def clean_code(self, *args, **kwargs):
        instance = self.instance
        code = self.cleaned_data.get('code')
        qs = Level.objects.filter(code__iexact=code)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This level has already been registered. Please try again.")
        return code


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['code', 'name']

    def clean_code(self, *args, **kwargs):
        instance = self.instance
        code = self.cleaned_data.get('code')
        qs = School.objects.filter(code__iexact=code)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This school has already been registered. Please try again.")
        return code

class ResultbookModelForm(forms.ModelForm):
    class Meta:
        model = Resultbook
        fields = ['student', 'semester', 'level', 'school', 'cgpa', 'gpa']

class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['parent', 'subject', 'grade']
