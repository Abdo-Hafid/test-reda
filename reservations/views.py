from django.shortcuts import render, get_object_or_404,redirect
from .models import Offre,Gallery,Reservation, client
from .forms import ClientForm, ReservationForm, ReservationStatusForm
from django.core.mail import send_mail
# Create your views here.
def home(request):
    last_offres = Offre.objects.all().order_by('-id')[:3]
    all_offres = Offre.objects.all()
    context = {
        'last_offres': last_offres,
        'all_offres': all_offres,
    }
    return render(request, 'index.html', context)
def gallery_view(request):
    images = Gallery.objects.all()  # Récupère toutes les images de la galerie
    return render(request, 'gallery.html', {'images': images})

def offer_detail(request, offer_id):
    offer = get_object_or_404(Offre, id=offer_id)
    
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if client_form.is_valid() and reservation_form.is_valid():
            client = client_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.client = client
            reservation.offre = offer
            reservation.save()

            return redirect('reservations:home')
    else:
        client_form = ClientForm()
        reservation_form = ReservationForm()

    return render(request, 'offer_detail.html', {
        'offer': offer,
        'client_form': client_form,
        'reservation_form': reservation_form
    })
def all_offers(request):
        offres = Offre.objects.all()
        return render(request, 'all_offers.html', {'offres': offres})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def gestion_reservations(request):
    reservations = Reservation.objects.all()
    
    # Filtrer par date de l'activité
    date_activite = request.GET.get('date_activite')
    if date_activite:
        reservations = reservations.filter(date_activite=date_activite)

    # Filtrer par statut
    status = request.GET.get('status')
    if status:
        reservations = reservations.filter(status=status)

    context = {
        'reservations': reservations,
    }
    
    return render(request, 'gestion_reservations.html', context)
def client_detail(request, client_id):
    client_detail = get_object_or_404(client, id=client_id)
    return render(request, 'client_detail.html', {'client': client_detail})
def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.method == 'POST':
        form = ReservationStatusForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations:gestion_reservations') 
    else:
        form = ReservationStatusForm(instance=reservation)

    return render(request, 'reservation_detail.html', {'reservation': reservation, 'form': form})