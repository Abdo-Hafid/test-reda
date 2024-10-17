from django import forms
from .models import client, Reservation

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['Prénom', 'name', 'email', 'adresse', 'ville', 'Region', 'code_postal', 'pays', 'cin_npassport', 'equitation_niv', 'assurance', 'numero_assurance']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_activite', 'participants', 'commentaire']
        widgets = {
            'date_activite': forms.DateInput(attrs={'type': 'date'}),
        }

class ReservationStatusForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=Reservation.status.field.choices),
        }
