from django.contrib import admin
from hondana.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn_code', 'title', 'publisher', 'author', 'translator', 'release_date', 'revision_date',)
    list_display_links = ('id', 'isbn_code', 'title',)
admin.site.register(Book, BookAdmin)
