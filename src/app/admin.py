from django.contrib import admin
from . models import Produit

# Enregistrer la table produit
@admin.register(Produit)
class ModelProduitAdmin(admin.ModelAdmin):
    list_display =['id','nom','prix_normal','categorie']