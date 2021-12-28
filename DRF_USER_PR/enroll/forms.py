from django import forms


class StudentRegisteration(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
