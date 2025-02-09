from django.db import models

# Create your models here.
class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, related_name='filieres')

    def __str__(self):
        return f"{self.nom}-({self.specialite.nom})"


class AnneeScolaire(models.Model):
    annee_scolaire = models.CharField(max_length=9)  # e.g., "2023-2024"


class Etudiant(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='etudiants')
    niveau = models.PositiveIntegerField()  # niveau d'étude (1,2,3,...)
    a_vote = models.BooleanField(default=False)
    annee_candidature = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE, related_name='etudiants')
    
    
    def __str__(self):
        return f"{self.nom} ({self.matricule})"


class Candidat(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE, primary_key=True)
    slogan = models.CharField(max_length=100)
    annee_candidature = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE, related_name='candidats')
    
    def __str__(self):
        return f"Candidat: {self.etudiant.nom} ({self.etudiant.matricule})"


class Vote(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)  # un étudiant ne vote qu'une fois
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name='votes')
    date_vote = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote de {self.etudiant.matricule} pour {self.candidat.etudiant.nom}"