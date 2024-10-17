from django.urls import path
from . import views
app_name = 'reservations'
urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('gallery/', views.gallery_view, name='gallery'),
    path('offres/', views.all_offers, name='all_offers'),
    path('offre/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gestion_reservations/', views.gestion_reservations, name='gestion_reservations'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'), 
]