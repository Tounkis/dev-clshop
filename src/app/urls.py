from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('categorie/<slug:val>', views.Categorie.as_view(), name="categorie"),
    path('detail/<int:id>', views.details, name="detail"),

]
