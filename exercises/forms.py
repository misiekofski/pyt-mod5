from django import forms
from .models import SCHOOL_CLASS


class SearchStudentForm(forms.Form):
    student = forms.CharField(label="Wyszukaj ucznia", max_length=20)


class AddStudentForm(forms.Form):
    name = forms.CharField(label="Imię", max_length=30)
    surname = forms.CharField(label="Nazwisko", max_length=40)
    klasa = forms.ChoiceField(choices=SCHOOL_CLASS)