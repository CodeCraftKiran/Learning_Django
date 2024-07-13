from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import books
# Create your views here.
def index(request):
    all_books = books.objects.all().order_by("-title")  # minus => -title is use for descending
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))
    
    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "total_num_of_books": num_books,
        "average_rating":avg_rating,
    })
    
def book_detail(request, slug):
    # book = books.objects.get(pk=id) 
    book = get_object_or_404(books, slug=slug) 
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })