from django import forms
from .models import book


class BookForm(forms.ModelForm):
    class Meta:
        model=book
        fields=['name','desc','price','img']