from django.shortcuts import render
from webapp.models import GuestBook



def index_view(request):
    guests_books = GuestBook.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={'guests_books': guests_books})


