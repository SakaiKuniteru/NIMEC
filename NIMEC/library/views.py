from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
from django.db.models import Q

def library(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        librarys = Book.objects.filter(
            Q(book_name__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(release_date__icontains=search_query)
        )
    else:
        librarys = Book.objects.all()
        
    paginator = Paginator(librarys, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "community/library/library.html", {
        'page_obj' : page_obj, 
        'search_query': search_query
        })

def library_detail(request, library_id):
    library = Book.objects.get(id=library_id)
    return render(request, "community/library/library_detail.html", {'library' : library})