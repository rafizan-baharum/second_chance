from django import forms

from portfolio.models import School
from .models import Resultbook, Result, Semester, Subject, Level


class SemesterModelForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['code', 'name']


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name']


class LevelModelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['code', 'name']


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['code', 'name']


class ResultbookModelForm(forms.ModelForm):
    class Meta:
        model = Resultbook
        fields = ['student', 'semester', 'level', 'school']


class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['parent', 'subject', 'grade']
