from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from library.models import Book, Dvd, Libuser, Libitem, Suggestion
from library.forms import SuggestionForm, SearchlibForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse


# Import necessary classes
# Create your views here.
def index(request):
    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, 'library/index.html', {'itemlist': itemlist, 'user':request.user})

def about(request):
    return render(request, 'library/about.html')

def detail(request, item_id):
    item = get_object_or_404(Libitem, id=item_id)
    return render(request, 'library/detail.html', {'item': item, 'user':request.user})

def suggestions(request):
    suggestionlist = Suggestion.objects.all()[:10]
    return render(request, 'library/suggestions.html', {'itemlist':suggestionlist, 'user':request.user})

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
            return render(request, 'library/newitem.html', {'form':form, 'suggestions':suggestions, 'user':request.user})
    else:
        form = SuggestionForm()
    return render(request, 'library/newitem.html', {'form':form, 'suggestions':suggestions, 'user':request.user})

def searchlib(request):
    form = SearchlibForm()
    itemlist=[]
    if request.method == 'POST':
        form = SearchlibForm(request.POST)
        if not form.is_valid():
            return render(request, 'library/searchlib.html', {'form':form, 'user':request.user})
        data = form.cleaned_data
        if data['author'] or data['title']:
            if data['author'] and data['title']:
                itemlist = Book.objects.filter(title__contains=data['title'], author=data['author'])
            else:
                if data['title']:
                    itemlist = Libitem.objects.filter(title__contains=data['title'])
                else:
                    itemlist = Book.objects.filter(author=data['author'])
    return render(request, 'library/searchlib.html', {'form':form, 'itemlist':itemlist, 'user':request.user})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('library:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return HttpResponseRedirect(reverse('library:index'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('library:index')))


@login_required
def myitems(request):
    items=[]
    message=''
    try:
        user = Libuser.objects.get(username = request.user.username)
        items = Libitem.objects.filter(user = user)
    except Libuser.DoesNotExist:
        message = 'You are not a Libuser!'
    return render(request, 'library/myitems.html', {'user':request.user, 'itemlist':items, 'message':message})
