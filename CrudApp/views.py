from django.shortcuts import render, redirect
from .forms import DepartementForm  # FormTache est la classe de formulaire dans forms.py
from .models import Departement  # Tache est le modèle pour les tâches

def index(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la tâche dans la base de données
            return redirect('/')  # Redirige vers la page index après l'ajout
    else:
        form = DepartementForm()  # Formulaire vide pour un GET

    list_departement = Departement.objects.all()

    context = {
        'form': form,  # Le formulaire à afficher
        'list_departement': list_departement  # La liste de toutes les tâches
    }
    return render(request, 'index.html', context)  # Affiche la page avec le formulaire et la liste des tâches

def edit_departement(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        departement = Departement.objects.get(id=id)
        form = DepartementForm(request.POST, instance=departement)
        if form.is_valid():
            form.save()
            return redirect('/')
    return redirect('/')

def delete_departement(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        departement = Departement.objects.get(id=id)
        departement.delete()
        return redirect('/')