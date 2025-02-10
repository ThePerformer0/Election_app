from django import forms

class LoginForm(forms.Form):
    is_student = forms.BooleanField(required=False, label='Je suis un étudiant')
    matricule = forms.CharField(label='Matricule', max_length=20, required=False)
    nom = forms.CharField(label='Nom', max_length=100, required=False)
    username = forms.CharField(label="Nom d'utilisateur", max_length=150, required=False)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput, required=False)