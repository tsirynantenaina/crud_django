from django import forms
from .models import Departement

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom', 'email', 'adresse', 'telephone']  # Les champs à inclure dans le formulaire

        # Optionnel : Ajouter des widgets pour personnaliser l'apparence des champs
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
