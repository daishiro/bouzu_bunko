from django.forms import ModelForm
from hondana.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('isbn_code', 'title', 'publisher', 'author', 'translator', 'release_date', 'revision_date',)
