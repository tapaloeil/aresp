from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
    

class Animal(models.Model):
    date_ajout =models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=200)
    espece = (
            ('CAT', 'Chat'),
            ('DOG','Chien'),
        )
    location = models.CharField(max_length=30)
    date_naissance = models.DateField(default=datetime.today)
    sexe_court_choice = (
            ('F', 'Femelle'),
            ('M', 'Male'),
        )
    sexe_court = models.CharField(
            max_length=1,
            choices=sexe_court_choice,
            default='F',
        )
    taille_choice=(
            ('S','Petit'),
            ('M','Moyen'),
            ('L','Grand'),
            ('XL','Très grand'),
        )
    origine = models.CharField(max_length=200)
    apparence = models.CharField(max_length=200)
    taille = models.CharField(
        max_length=2,
        choices=taille_choice,
        default='M',
        )
    temperament = models.CharField(max_length=200)
    num_puce = models.CharField(max_length=100)
    statut_choice=(
            ('01','à adopter'),
            ('02','en attente'),
            ('03','adopté'),
            ('04','inactif'),
        )
    statut = models.CharField(
        max_length=2,
        choices=statut_choice,
        default='01',
        )
    description = models.TextField

    def __str__(self):
        return self.nom