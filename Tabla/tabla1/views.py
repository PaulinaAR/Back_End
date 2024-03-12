from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {'username': 'Hola desde views.py'}
    return render(request, 'tabla1/tabla.html', context=my_context)