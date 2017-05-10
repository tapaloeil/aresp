from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
    

class Animal(models.Model):
    nom = models.CharField(max_length=200)
    espece_choix = (
            ('CAT', 'Chat'),
            ('DOG','Chien'),
        )
    espece = models.CharField(
            max_length=3,
            choices=espece_choix,
            default='CAT',
        )
    date_naissance = models.DateField(default=datetime.today)
    sexe_court_choice = (
            ('F', 'Femelle'),
            ('M', 'Male'),
        )
    sexe = models.CharField(
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
    taille = models.CharField(
        max_length=2,
        choices=taille_choice,
        default='M',
        )   
    origine = models.CharField(max_length=200)
    location = models.CharField(max_length=30) 
    apparence = models.CharField(max_length=200)
    temperament = models.CharField(max_length=200)
    num_puce = models.CharField(max_length=100, blank=True, null=True)
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
    description = models.TextField(blank=True,null=True)
    date_ajout =models.DateTimeField(auto_now_add=True)
    user_ajout = models.ForeignKey('auth.User',null=True)
    date_publication = models.DateTimeField(blank=True,null=True,editable=False)

    def publier(self):
        self.date_publication=timezone.now()
        self.save()

    def __str__(self):
        return self.nom