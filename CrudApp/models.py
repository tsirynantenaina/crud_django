from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100)  # Nom du département
    email = models.EmailField()  # Email du département
    adresse = models.TextField()  # Adresse du département
    telephone = models.CharField(max_length=15)  # Numéro de téléphone du département

    def __str__(self):
        return self.nom  # Affiche le nom du département dans l'administration
