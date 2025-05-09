from django import forms
from .models import Book, Author, Exampler, Genre



class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите название жанра'})
        }

class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': 6}),
        required=True
    )

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'rating', 'date_of_publish', 'authors', 'genres']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'date_of_birth', 'date_of_death', 'place_of_birth', 'biography']

class ExamplerForm(forms.ModelForm):
    class Meta:
        model = Exampler
        fields = ['inventory_number', 'book', 'condition']
