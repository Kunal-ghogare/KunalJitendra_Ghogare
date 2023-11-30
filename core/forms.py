from django import forms
from .models import Contact

class AddContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ("name", "email", "created")
        widgets = {
            'name':forms.TextInput(attrs= {'class': 'form-control'}),
            'email':forms.TextInput(attrs= {'class': 'form-control'}),
            'created':forms.TextInput(attrs= {'class': 'form-control'})
        }
