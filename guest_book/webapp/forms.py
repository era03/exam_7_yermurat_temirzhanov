from django import forms
from django.forms import CharField, widgets



class GuestBookForm(forms.Form):
    author = CharField(max_length=50, required=True, label='Author', widget=forms.TextInput({'class': 'form-input'}))
    email = CharField(max_length=50, required=True, label='Email',)
    text = CharField(max_length=5000, required=True, label='Text', widget=widgets.Textarea)
