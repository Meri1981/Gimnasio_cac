from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
         "gimnasio" : "Gimnasio CaC" }
    return render(request, "web/index.html", context)



def registrarse(request):
    contexto ={}
    if request.method == 'GET':
            contexto['registrarse_form'] = RegistrarseForm()
    else: #asumimos que es un POST
        form = RegistrarseForm(request.POST)
        contexto['registrarse_form'] = form
        if form.is_valid():

            messages.success(request, "Se ha registrado con éxito")

        #print(request.POST)
            return redirect('index')
    return render(request, 'web/registrarse.html', contexto)