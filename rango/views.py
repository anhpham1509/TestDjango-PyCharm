from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return

