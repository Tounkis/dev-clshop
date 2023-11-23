from django.db import models

# Creation de la table des produits.
CATEGORIE = (
  ('ordinateur','ORDINATEUR'),
  ('telephone','TELEPHONE'),
  ('tablette','TABLETTE'),
  ('electromenager','ELECTROMENAGER'),
)

class Produit(models.Model):
  nom = models.CharField(max_length=100)
  prix_normal = models.FloatField()
  prix_promo = models.FloatField()
  description = models.TextField(default='')
  caracteristique = models.TextField(default='')
  categorie = models.CharField(choices= CATEGORIE, max_length=50)
  image = models.ImageField(upload_to='produit')
  def __str__(self):
      return self.nom