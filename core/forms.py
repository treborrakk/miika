from django import forms

from .models import Subject
from core.models import Subject, LookupType, Lookup
from .models import *

year_level_lov = LookupType.objects.filter(name='YEAR_LEVEL').first()
# subject_code_lov = LookupType.objects.filter(name='SUBJECT_CODE').first()
subject_type_lov = LookupType.objects.filter(name='SUBJECT_TYPE').first()

class SubjectForm(forms.ModelForm):
    year_level = forms.ModelChoiceField(
        label="Types of Year Level",
        # widget=forms.Select,
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Lookup.objects.filter(lookup_type_id=year_level_lov.id),
        required=True,
        to_field_name='value'
    )
    # subject_code = forms.ModelChoiceField(
    #     label="Subject Code",
    #     # widget=forms.Select,
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     queryset=Lookup.objects.filter(lookup_type_id=subject_code_lov.id),
    #     required=True,
    #     to_field_name='value'
    # )

    subject_type = forms.ModelChoiceField(
        label="Subject Type",
        # widget=forms.Select,
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Lookup.objects.filter(lookup_type_id=subject_type_lov.id),
        required=True,
        to_field_name='value'
    )
    class Meta:
        model = Subject
        fields = ('year_level', 'subject_code', 'subject_description', 'lesson_number', 'lesson_name', 'cover', 'file',
                  'subject_type')
        widgets = {'year_level': forms.TextInput(attrs={ 'class': 'form-control','id':'id_year_level' }),
                   'subject_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_subject_code'}),
                   'subject_description': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_subject_description'}),
                   'lesson_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_year_level'}),
                   'lesson_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_lesson_name'}),
                   'subject_type': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_subject_type'})
                   }