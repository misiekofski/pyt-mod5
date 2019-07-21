from django import forms
from django.forms import CheckboxSelectMultiple, RadioSelect

from exercises.models import SCHOOL_CLASS


class SearchStudentForm(forms.Form):
    last_name = forms.CharField(label="Wyszukaj po nazwisku", max_length=64)


class AddStudentForm(forms.Form):
    name = forms.CharField(label="Imię", max_length=30)
    surname = forms.CharField(label="Nazwisko", max_length=40)
    klasa = forms.ChoiceField(choices=SCHOOL_CLASS)


TOPPINGS=(
    (1, "Oliwki"),
    (2, "Pomidory"),
    (3, "Dodatkowy ser"),
    (4, "Cebula"),
    (5, "Anszua"),
    (6, "Wincyj Cebuli"),
    )


class PizzaToppingsForm(forms.Form):
    toppings = forms.MultipleChoiceField(choices=TOPPINGS, widget=CheckboxSelectMultiple)


class UserValidationForm(forms.Form):
    first_name = forms.CharField(label="Imie", max_length=64)
    last_name = forms.CharField(label="Nazwisko", max_length=64)
    email = forms.EmailField(label="Email", max_length=64)
    url = forms.URLField(label="WWW", max_length=100)
