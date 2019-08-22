from django import forms

from .models import Student, City, State


class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['code', 'name']


class StateModelForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['code', 'name']


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nric_no', 'name', 'nick_name', 'gender', 'religion', 'race',
                  'address1', 'address2', 'address3', 'city', 'state',
                  'school',
                  'bank', 'bank_account_no',
                  'father_name', 'father_nric_no', 'father_race', 'father_religion', 'father_income',
                  'mother_name', 'mother_nric_no', 'mother_race', 'mother_religion', 'mother_income',
                  'birth_date',
                  'registered_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'registered_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nric_no(self, *args, **kwargs):
        instance = self.instance
        nric_no = self.cleaned_data.get('nric_no')
        qs = Student.objects.filter(nric_no__iexact=nric_no)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This nricno has already been registered. Please try again.")
        return nric_no
