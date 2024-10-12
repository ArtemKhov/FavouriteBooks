from django import forms
from django.core.exceptions import ValidationError

from .models import Book, Genres

class AddBookForm(forms.ModelForm):
    genres = forms.ModelChoiceField(queryset=Genres.objects.all().order_by('genre'),
                                    label='Genres',
                                    empty_label=None,
                                    widget=forms.SelectMultiple(attrs={'class': 'genres-option'}))

    class Meta:
        model = Book
        fields = ['title', 'description', 'is_published']
        labels = {
            'title': 'Book name',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Opinion about the book', 'class': 'description-form'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        title_length = 100
        if len(title) > title_length:
            raise ValidationError(f'The length of the Book name cannot exceed {title_length} characters')

        return title