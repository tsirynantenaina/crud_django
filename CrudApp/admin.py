from django.contrib import admin
from .models import Departement

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email','adresse', 'telephone')  # Champs affichés dans l'admin
