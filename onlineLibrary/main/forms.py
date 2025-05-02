from django import forms
from .models import Reader

class LoginForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'surname', 'date_of_birth', 'email', 'number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
