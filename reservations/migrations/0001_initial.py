# Generated by Django 4.2.7 on 2024-10-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prénom', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('Region', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('cin_npassport', models.CharField(blank=True, max_length=100, null=True)),
                ('equitation_niv', models.CharField(choices=[('0/3', '0/3'), ('1/3', '1/3'), ('2/3', '2/3'), ('3/3', '3/3')], max_length=20, null=True)),
                ('assurance', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_assurance', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('date_activite', models.DateField()),
                ('participants', models.PositiveIntegerField()),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('En attente', 'En attente'), ('Confirmée', 'Confirmée'), ('Annulée', 'Annulée')], default='En attente', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.client')),
                ('offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.offre')),
            ],
        ),
    ]
