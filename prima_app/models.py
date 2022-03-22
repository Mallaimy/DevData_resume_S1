from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

CHOICES_M = (
        ('F', 'Femme'),
        ('H', 'Homme'),)

CHOICES_C = (
        ('Echo abdominal', 'Echo abdominal'),
        ('Echo Pelvienne', 'Echo Pelvienne'),
        ('Echo Arbre urinaire', 'Echo Arbre urinaire'),
        ('Echo Obstétricale', 'Echo Obstétricale'),
        ('Echo Obstétrical 3D/4D', 'Echo Obstétrical 3D/4D'),
        ('Echo mamaire(sein)', 'Echo mamaire(sein)'),
        ('Echo parties moles', 'Echo parties moles'),
        ('Echo bourses(Testicules)', 'Echo bourses (Testicules)'),
        ('Echo épaule-Genoux', 'Echo épaule-Génoux'),
        ('Echo Doppler', 'Echo Doppler'),
        ('TSA','TSA'),
        ('Membre inférieur', 'Membre inférieur'),
        ('Membres inférieur', 'Membres inférieur'),
        ('Bourses', 'Bourses'),
        )

class Medecin(models.Model):
    nom_prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=40, choices= CHOICES_M )
    specialité = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_prenom

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nom_prenom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=40, choices =CHOICES_M)
    age = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    categorie_imagerie = models.CharField(max_length=50, choices=CHOICES_C)
    prix = models.FloatField()
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True, blank=True)
    decription_res = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.nom_prenom

    class Meta:
        ordering = ['date']
    