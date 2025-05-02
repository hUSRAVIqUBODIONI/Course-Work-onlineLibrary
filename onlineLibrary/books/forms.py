from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'description', 'rating', 'date_of_publish']
        widgets = {
            'date_of_publish': forms.DateInput(attrs={'type': 'date'}),
        }
