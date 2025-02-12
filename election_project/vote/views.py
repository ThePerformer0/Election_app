from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            is_student = form.cleaned_data.get('is_student')
            if is_student:
                matricule = form.cleaned_data['matricule']
                nom = form.cleaned_data['nom']
                try:
                    etudiant = Etudiant.objects.get(matricule=matricule, nom=nom)
                    request.session['etudiant_matricule'] = etudiant.matricule
                    return redirect('vote_page')
                except Etudiant.DoesNotExist:
                    messages.error(request, "Identifiants incorrects")
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.is_staff:
                        return redirect('admin_panel')
                    else:
                        return redirect('vote_page')
                else:
                    messages.error(request, "Identifiants incorrects")
    else:
        form = LoginForm()
    return render(request, 'vote/login.html', {'form': form})


def vote_view(request):
    etudiant_matricule = request.session.get("etudiant_matricule")
    if not etudiant_matricule:
        return redirect('login_view')
    
    etudiant = get_object_or_404(Etudiant, matricule=etudiant_matricule)
    
    # Vérification que l'étudiant n'a pas déjà voté
    if etudiant.a_vote:
        messages.info(request, "Vous avez déjà voté.")
        return redirect('vote_status')
    
    # Sélection des candidats : par exemple, ceux dont le niveau est >= 3
    candidats = Candidat.objects.filter(annee_candidature=etudiant.annee_scolaire)
    
    if request.method == "POST":
        candidat_matricule = request.POST.get("candidat_matricule")
        try:
            candidat = get_object_or_404(Candidat, etudiant__matricule=candidat_matricule)
            # Enregistrement du vote
            Vote.objects.create(etudiant=etudiant, candidat=candidat)
            etudiant.a_vote = True
            etudiant.save()
            messages.success(request, "Votre vote a été enregistré.")
            return redirect('vote_status')
        except Candidat.DoesNotExist:
            messages.error(request, "Candidat invalide.")
    
    return render(request, "vote/vote.html", {"candidats": candidats, "etudiant": etudiant})


def vote_status(request):
    etudiant_matricule = request.session.get("etudiant_matricule")
    if not etudiant_matricule:
        return redirect('login_view')
    etudiant = get_object_or_404(Etudiant, matricule=etudiant_matricule)
    vote = Vote.objects.filter(etudiant=etudiant).first()
    return render(request, "vote/vote_status.html", {"vote": vote})



@staff_member_required
def admin_panel(request):
    total_etudiants = Etudiant.objects.count()
    total_votes = Vote.objects.count()
    
    filiere_sic = Filiere.objects.filter(nom__icontains="sécurité informatique").first()
    non_votants = Etudiant.objects.filter(filiere=filiere_sic, a_vote=False).count() if filiere_sic else 0
    
    # Initialisation des formulaires
    etudiant_form = EtudiantForm()
    candidat_form = CandidatForm()
    
    # Formulaires pour ajouter des étudiants et des candidats
    if request.method == 'POST':
        if 'add_etudiant' in request.POST:
            etudiant_form = EtudiantForm(request.POST)
            if etudiant_form.is_valid():
                Etudiant.objects.create(
                    matricule=etudiant_form.cleaned_data['matricule'],
                    nom=etudiant_form.cleaned_data['nom'],
                    filiere=etudiant_form.cleaned_data['filiere'],
                    niveau=etudiant_form.cleaned_data['niveau'],
                    annee_scolaire=etudiant_form.cleaned_data['annee_scolaire']
                )
                messages.success(request, "Étudiant ajouté avec succès.")
                return redirect('admin_panel')
        elif 'add_candidat' in request.POST:
            candidat_form = CandidatForm(request.POST, request.FILES)
            if candidat_form.is_valid():
                etudiant = candidat_form.cleaned_data['etudiant']
                if Candidat.objects.filter(etudiant=etudiant).exists():
                    messages.error(request, "Cet étudiant est déjà candidat.")
                else:
                    Candidat.objects.create(
                        etudiant=etudiant,
                        slogan=candidat_form.cleaned_data['slogan'],
                        annee_candidature=candidat_form.cleaned_data['annee_candidature'],
                        photo=candidat_form.cleaned_data['photo']
                    )
                    messages.success(request, "Candidat ajouté avec succès.")
                return redirect('admin_panel')
        elif 'delete_candidat' in request.POST:
            candidat_matricule = request.POST.get("candidat_matricule")
            candidat = get_object_or_404(Candidat, etudiant__matricule=candidat_matricule)
            candidat.delete()
            messages.success(request, "Candidat supprimé avec succès.")
            return redirect('admin_panel')
    
    # Statistiques de vote
    candidats = Candidat.objects.all()
    votes_par_candidat = {candidat: Vote.objects.filter(candidat=candidat).count() for candidat in candidats}
    specialites = Specialite.objects.all()
    votes_par_specialite = {
        specialite: {
            'total': Etudiant.objects.filter(filiere__specialite=specialite).count(),
            'votants': Etudiant.objects.filter(filiere__specialite=specialite, a_vote=True).count()
        }
        for specialite in specialites
    }
    
    context = {
        "total_etudiants": total_etudiants,
        "total_votes": total_votes,
        "non_votants": non_votants,
        "etudiant_form": etudiant_form,
        "candidat_form": candidat_form,
        "votes_par_candidat": votes_par_candidat,
        "votes_par_specialite": votes_par_specialite,
    }
    return render(request, "vote/admin_panel.html", context)

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('login_view')
