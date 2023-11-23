from django.shortcuts import render
from django.views import View
from . models import Produit

# Fonction pour afficher la page d'accuiel
def home(request):
    return render(request, "home.html")

# Fonction pour afficher la page A propos
def about(request):
    return render(request, "about.html")

# Fonction pour afficher la page contact
def contact(request):
    return render(request, "contact.html")

# Fonction pour afficher la page des detail produits
class Categorie(View):
    def get(self, request, val):
        produits = Produit.objects.filter(categorie=val)
        nom = Produit.objects.filter(categorie=val).values('nom')
        return render(request, "category.html", locals())

# fonction pour afficher les detail du produit
def details(request):
    pass

