from django.contrib import admin
from .models import Offre, Gallery, client, Reservation, OptionPrix

# Inline pour ajouter et gérer les options de prix dans l'offre
class OptionPrixInline(admin.TabularInline):
    model = OptionPrix
    extra = 1  # Nombre de lignes supplémentaires vides pour ajouter de nouveaux choix

# Configuration de l'interface d'administration pour le modèle Offre
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')  # Champs affichés dans la liste des offres
    search_fields = ('name', 'description')  # Permet de rechercher par nom et description
    inlines = [OptionPrixInline]  # Ajout des options de prix directement dans la page d'offre

# Configuration de l'interface d'administration pour le modèle Gallery
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

# Configuration de l'interface d'administration pour le modèle Client
@admin.register(client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'Prénom', 'email', 'ville', 'pays')  # Champs affichés dans la liste des clients
    search_fields = ('name', 'email')  # Recherche par nom et email

# Configuration de l'interface d'administration pour le modèle Reservation
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'offre', 'date_reservation', 'date_activite', 'status', 'participants')  # Champs affichés dans la liste des réservations
    search_fields = ('client__name', 'offre__name')  # Permet de rechercher par nom du client et de l'offre
    list_filter = ('status', 'date_activite')  # Ajout de filtres par statut et date de l'activité
