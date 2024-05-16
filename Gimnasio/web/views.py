from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.
def index(request):
    context = {
         'gimnasio' : 'Gimnasio CAC'
    }
    return render(request, "web/index.html", context)

def registrarse(request):
    contexto ={}
    if request.method == 'GET':
            contexto['registrarse_form'] = RegistrarseForm()
    else: #asumimos que es un POST
        contexto['registrarse_form'] = RegistrarseForm(request.POST)

        print(request.POST)
        return redirect('index')
    return render(request, 'web/registrarse.html', contexto)