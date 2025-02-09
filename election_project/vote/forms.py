from django import forms

class LoginForm(forms.Form):
    matricule = forms.CharField(label='Matricule', max_length=20)
    nom = forms.CharField(label='Nom', max_length=100)