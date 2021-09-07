from django.shortcuts import render

# Create your views here.
from symbols.models import Symbol
from symbols import forms


def search(request):
    search_results = []
    symbols = Symbol.objects.all()
    if request.method == 'GET':  # If the form is submitted
        keyword = request.GET.get('search_box', None)
        for i in symbols:
            if i.name == str(keyword):
                search_results.append(i)

    return render(request, 'search_result.html', {
        "search_results": search_results
    })


def home(request):
    form = forms.AddSymbolForm()
    """views the home page"""
    symbols = Symbol.objects.order_by('index')
    return render(request, "home.html", {
        "symbols": symbols,
        "form": form,
    })


types = ['INT', 'ID', 'NUM', 'FUNCTION']


def get_index(name):
    # also deletes the one to be replaced
    index = ''.join(str(ord(c)) for c in str(name))  # concat the asci values
    index = int(index) % 11  # makes index up to 10
    return index


def delete_symbol(request, symbol_id):
    Symbol.objects.get(pk=symbol_id).delete()
    return home(request)


def form_checker(request, instance):
    text = instance.name
    result = [x.strip() for x in text.split(',')]
    return result


def add_symbol(request):
    if request.method == "POST":
        form = forms.AddSymbolForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            result = form_checker(request, instance)
            if len(result) == 2:
                print('creating...')
                name = result[0]
                type = result[1]
                if type in types:
                    # instance is valid so lets make its index and also remove duplicates
                    instance.index = get_index(name)
                    instance.name = name
                    instance.type = type
                    if type == 'num':
                        instance.size = 4
                    elif type == 'id':
                        instance.size = 1
                    instance.save()
                else:
                    return home(request)
            else:
                return home(request)
            return home(request)
    else:
        return home(request)
