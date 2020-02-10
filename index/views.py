from django.shortcuts import render
from .forms import Data
from .function import func


def index(request):
    if request.method == 'GET':
        new_form = Data()
        return render(request, 'index.html', {'new_form': new_form})
    elif request.method == 'POST':
        form = Data(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            new = func(data)
            return render(request, 'index.html', {'data': new})

