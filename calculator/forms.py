from django.forms import ModelForm
from .models import *
from django import forms

class SalaryForm(forms.Form):

    class Meta():
        ...

    monthly_salary = forms.IntegerField(help_text = "Introduce the number without any commas.")
    bonifications = forms.IntegerField(help_text = "Introduce the number without any commas.")
    Overtime = forms.IntegerField(help_text = "Introduce the number without any commas.")
