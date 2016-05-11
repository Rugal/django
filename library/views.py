from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book, Dvd, Libuser, Libitem

# Import necessary classes
# Create your views here.
def index(request):
    booklist = Book.objects.all() [:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of books: ' + '</p>'
    response.write(heading1)
    for book in booklist:
        para = '<p>' + str(book) + '</p>'
        response.write(para)
    return response
