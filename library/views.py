from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book, Dvd, Libuser, Libitem, Suggestion
from library.forms import SuggestionForm, SearchlibForm
from django.shortcuts import get_object_or_404


# Import necessary classes
# Create your views here.
def index(request):
    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, 'library/index.html', {'itemlist': itemlist})

def about(request):
    return render(request, 'library/about.html')

def detail(request, item_id):
    item = get_object_or_404(Libitem, id=item_id)
    return render(request, 'library/detail.html', {'item': item})

def suggestions(request):
    suggestionlist = Suggestion.objects.all()[:10]
    return render(request, 'library/suggestions.html', {'itemlist':suggestionlist})

def newitem(request):
    suggestions = Suggestion.objects.all()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.num_interested = 1
            suggestion.save()
            return HttpResponseRedirect(reverse('library:suggestions'))
        else:
            return render(request, 'library/newitem.html', {'form':form, 'suggestions':suggestions})
    else:
        form = SuggestionForm()
    return render(request, 'library/newitem.html', {'form':form, 'suggestions':suggestions})

def searchlib(request):
    form = SearchlibForm()
    itemlist=[]
    if request.method == 'POST':
        form = SearchlibForm(request.POST)
        if not form.is_valid():
            return render(request, 'library/searchlib.html', {'form':form})
        data = form.cleaned_data
        if data['author'] or data['title']:
            if data['author'] and data['title']:
                itemlist = Book.objects.filter(title__contains=data['title'], author=data['author'])
            else:
                if data['title']:
                    itemlist = Book.objects.filter(title__contains=data['title'])
                else:
                    itemlist = Book.objects.filter(author=data['author'])
    return render(request, 'library/searchlib.html', {'form':form, 'itemlist':itemlist})
