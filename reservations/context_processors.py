from .models import Offre

def offres_in_menu(request):
    all_offres = Offre.objects.all()  # Toutes les offres pour le menu
    return {
        'all_offres': all_offres
    }