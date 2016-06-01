from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book, Dvd, Libuser, Libitem
from django.shortcuts import get_object_or_404

# Import necessary classes
# Create your views here.
def index(request):
    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, 'library/index.html', {'itemlist': itemlist})

def about(request):
    return render(request, 'library/about.html')

def detail(request, item_id):
    try:
        item = Libitem.objects.get(id=item_id)
    except Exception as e:
        return get_object_or_404(Libitem, id=item_id)
