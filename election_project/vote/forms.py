from django import forms
from .models import *

class LoginForm(forms.Form):
    is_student = forms.BooleanField(required=False, label='Je suis un étudiant')
    matricule = forms.CharField(label='Matricule', max_length=20, required=False)
    nom = forms.CharField(label='Nom', max_length=100, required=False)
    username = forms.CharField(label="Nom d'utilisateur", max_length=150, required=False)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput, required=False)

class EtudiantForm(forms.Form):
    matricule = forms.CharField(label='Matricule', max_length=20)
    nom = forms.CharField(label='Nom', max_length=100)
    filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), label='Filière')
    niveau = forms.IntegerField(label='Niveau')
    annee_scolaire = forms.ModelChoiceField(queryset=AnneeScolaire.objects.all(), label='Année Scolaire')

class CandidatForm(forms.Form):
    etudiant = forms.ModelChoiceField(queryset=Etudiant.objects.all(), label='Étudiant')
    slogan = forms.CharField(label='Slogan', max_length=100)
    annee_candidature = forms.ModelChoiceField(queryset=AnneeScolaire.objects.all(), label='Année de Candidature')
    photo = forms.ImageField(label='Photo', required=False)