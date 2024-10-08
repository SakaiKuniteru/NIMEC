from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def library(request):
    librarys = Book.objects.all()
    return render(request, "community/library/library.html", {'librarys' : librarys})

def library_detail(request, library_id):
    library = Book.objects.get(id=library_id)
    return render(request, "community/library/library_detail.html", {'library' : library})