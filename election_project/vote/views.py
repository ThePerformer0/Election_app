from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import LoginForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            matricule = form.cleaned_data['matricule']
            nom = form.cleaned_data['nom']
            try:
                etudiant = Etudiant.objects.get(matricule=matricule, nom=nom)    
                request.session['etudiant_id'] = etudiant.id
                return redirect('vote:vote')
            except Etudiant.DoesNotExist:
                messages.error(request, "Identifiants incorrects")
    else:
        form = LoginForm()
    return render(request, 'vote/login.html', {'form': form})


def vote_view(request):
    etudiant_id = request.session.get("etudiant_id")
    if not etudiant_id:
        return redirect('login_view')
    
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    
    # Vérification que l'étudiant n'a pas déjà voté
    if etudiant.a_vote:
        messages.info(request, "Vous avez déjà voté.")
        return redirect('vote_status')
    
    # Sélection des candidats : par exemple, ceux dont le niveau est >= 3
    candidats = Candidat.objects.filter(annee_candidature=etudiant.annee_scolaire)
    
    if request.method == "POST":
        candidat_id = request.POST.get("candidat")
        try:
            candidat = Candidat.objects.get(pk=candidat_id)
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
    etudiant_id = request.session.get("etudiant_id")
    if not etudiant_id:
        return redirect('login_view')
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    vote = Vote.objects.filter(etudiant=etudiant).first()
    return render(request, "vote/vote_status.html", {"vote": vote})



@staff_member_required
def admin_panel(request):
    total_etudiants = Etudiant.objects.count()
    total_votes = Vote.objects.count()
    
    # Exemple : nombre d'étudiants de la filière "sécurité informatique" qui n'ont pas voté
    filiere_sic = Filiere.objects.filter(nom__icontains="sécurité informatique").first()
    non_votants = Etudiant.objects.filter(filiere=filiere_sic, a_vote=False).count() if filiere_sic else 0
    
    context = {
        "total_etudiants": total_etudiants,
        "total_votes": total_votes,
        "non_votants": non_votants,
    }
    return render(request, "vote/admin_panel.html", context)

