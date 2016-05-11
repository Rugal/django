from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book, Dvd, Libuser, Libitem
from django.shortcuts import get_object_or_404

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


def about(request):
    response = HttpResponse()
    response.write('This is a Library APP.')
    return response

def detail(request, item_id):
    try:
        item = Libitem.objects.get(id=item_id)
    except Exception as e:
        return get_object_or_404(Libitem, id=item_id)
    response = HttpResponse()
    response.write('<table>')
    response.write('<tr><td>title</td><td>'+ item.title +'</td></tr>')
    response.write('<tr><td>duedate</td><td>'+ str(item.duedate) +'</td></tr>')
    try:
        response.write('<tr><td>author</td><td>'+ Book.objects.get(id=item_id).author +'</td></tr>')
    except Exception as e:
        response.write('<tr><td>maker</td><td>'+ Dvd.objects.get(id=item_id).maker +'</td></tr>')
    response.write('</table>')
    return response

