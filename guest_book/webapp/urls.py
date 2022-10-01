from unicodedata import name
from django.contrib import admin
from django.urls import path
from webapp.views.base import index_view
from webapp.views.guest_book import guest_book_add_view, guest_book_edit_view, guest_book_delete, guest_book_confirm_delete


urlpatterns = [
    path('', index_view, name='index'),
    path('add/', guest_book_add_view, name='guest_book_add'),
    path('edit/<int:pk>/', guest_book_edit_view, name='guest_book_edit'),
    path('delete/<int:pk>/', guest_book_delete, name='guest_book_delete'),
    path('delete/<int:pk>/confirm_delete/', guest_book_confirm_delete ,name='guest_book_confirm_delete')
]