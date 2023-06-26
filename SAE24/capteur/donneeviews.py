
from .forms import DonneesForm
from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request):
    liste = list(models.Donnees.objects.all())
    return render(request, 'Donnees/index.html',{'liste': liste})


def ajout(request):
    if request.method == "POST":
        form = DonneesForm(request)
        if form.is_valid():
            Donnees = form.save()
            return render(request, "Donnees/affiche.html", {"Donnees": Donnees})
        else:
            return render(request, "Donnees/ajout.html", {"form": form})
    else:
        form = DonneesForm()
        return render(request, "Donnees/ajout.html", {"form": form})

def affiche(request, id):
    Donnees = models.Donnees.objects.get(pk=id)
    return render(request, "Donnees/affiche.html", {"Donnees": Donnees})