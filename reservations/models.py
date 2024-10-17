from django.db import models

# Modèle pour les offres d'activités
class Offre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Corrigé le chemin vers images
    
    def __str__(self):
        return self.name

# Modèle pour la galerie d'images
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    
    def __str__(self):
        return str(self.image)

# Modèle pour les clients
class client(models.Model):  # Correction ici, "client" devient "Client"
    Prénom = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    cin_npassport = models.CharField(max_length=100, blank=True, null=True)
    equitation_niv = models.CharField(max_length=20, choices=(('0/3', '0/3'), ('1/3', '1/3'),('2/3', '2/3'), ('3/3', '3/3')), null=True)
    assurance = models.CharField(max_length=100, blank=True, null=True)
    numero_assurance = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

# Modèle pour les réservations
class Reservation(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE)  # Lien avec le modèle Client
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)  # Lien avec le modèle Offre
    date_reservation = models.DateTimeField(auto_now_add=True)  # Date de réservation
    date_activite = models.DateField()  # Date de l'activité réservée
    participants = models.PositiveIntegerField()  # Nombre de participants
    commentaire = models.TextField(blank=True, null=True)  # Commentaire supplémentaire du client
    status = models.CharField(
        max_length=20, 
        choices=(('En attente', 'En attente'), ('Confirmée', 'Confirmée'), ('Annulée', 'Annulée')),
        default='En attente'
    )

    def __str__(self):
        return f"Réservation de {self.client.name} pour {self.offre.name}"

# Modèle pour les options de prix
class OptionPrix(models.Model):
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name='options_prix')  # Lien avec le modèle Offre
    description = models.CharField(max_length=100)  # Description de l'option (ex: "1 Heure", "2 Heures coucher du soleil")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix associé à cette option

    def __str__(self):
        return f"{self.description} - {self.price} €"
