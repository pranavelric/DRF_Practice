from django import forms
from .models import User
from django.core import validators

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User
        fields =  ['id', 'name', 'email', 'password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
