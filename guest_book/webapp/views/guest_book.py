from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import GuestBook
from webapp.forms import GuestBookForm



def guest_book_add_view(request):
    form = GuestBookForm()
    if request.method == 'GET':
        return render(request, 'guest_book_add.html', context={'form': form})
    form = GuestBookForm(request.POST)
    if not form.is_valid():
        return render(request, 'guest_book_add.html', context={'form': form})
    GuestBook.objects.create(**form.cleaned_data)
    return redirect('index')


def guest_book_edit_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(initial={
            'author': guest_book.author,
            'email': guest_book.email,
            'text': guest_book.text
        })
        return render(request, 'guest_book_edit.html', context={'form': form, 'guest_book': guest_book})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest_book.author = form.cleaned_data['author']
            guest_book.email = form.cleaned_data['email']
            guest_book.text = form.cleaned_data['text']
            guest_book.save()
            return redirect('index')
        else:
            return render(request, 'guest_book_edit.html', context={'form': form, 'guest_book': guest_book})


def guest_book_delete(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'guest_book_confirm_delete.html', context={'guest_book': guest_book})


def guest_book_confirm_delete(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    guest_book.delete()
    return redirect('index')