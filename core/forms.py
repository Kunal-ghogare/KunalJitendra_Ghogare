from django import forms
from .models import Contact
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class AddContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ("name", "email", "created")
        widgets = {
            'name':forms.TextInput(attrs= {'class': 'form-control'}),
            'email':forms.TextInput(attrs= {'class': 'form-control'}),
            'created':DateInput()
        }
