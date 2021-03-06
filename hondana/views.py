from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from hondana.models import Book
from hondana.forms import BookForm


@login_required
def book_list(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'hondana/book_list.html', {'books': books})


@login_required
def book_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('hondana:book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'hondana/book_edit.html', dict(form=form, book_id=book_id))


@login_required
def book_del(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('hondana:book_list')
