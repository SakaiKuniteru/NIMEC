from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name', 'image_book', 'book_description',
            'author', 'release_date', 'book_price'
        ]
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_book_price(self):
        book_price = self.cleaned_data.get('book_price')

        if isinstance(book_price, str):
            book_price = book_price.replace('.', '')

        try:
            book_price = int(book_price)
        except ValueError:
            raise forms.ValidationError("Giá bán phải là một số hợp lệ.")
        
        return book_price