from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),  # Associe la vue 'index' à la route racine
    path('edit/', views.edit_departement, name='edit_departement'),
    path('delete/', views.delete_departement, name='delete_departement'),
]