from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
from tinymce.models import HTMLField
 
def upload_location(instance, filename):
    return "Animal/%s/%s/%s" %(instance.espece,instance.pk,filename)

class Animal(models.Model):
    nom = models.CharField(max_length=200, verbose_name='Nom')
    espece_choix = (
            ('CAT', 'Chat'),
            ('DOG','Chien'),
        )
    espece = models.CharField(
            max_length=3,
            choices=espece_choix,
            default='CAT',
            verbose_name='Espèce'
        )
    date_naissance = models.DateField(default=datetime.today, verbose_name='Date de naissance')
    sexe_court_choice = (
            ('F', 'Femelle'),
            ('M', 'Male'),
        )
    sexe = models.CharField(
            max_length=1,
            choices=sexe_court_choice,
            default='F',
            verbose_name='Sexe',
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
        verbose_name='Taille'
        )   
    origine = models.CharField(max_length=200, verbose_name="Origine de l'animal")
    location = models.CharField(max_length=30, verbose_name='Localisation actuelle') 
    apparence = models.CharField(max_length=200, verbose_name='Apparence')
    temperament = models.CharField(max_length=200, verbose_name='Tempérament')
    num_puce = models.CharField(max_length=100, blank=True, null=True, verbose_name='Numéro de puce')
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
        verbose_name="Statut de l'animal"
        )
    description = models.TextField(blank=True,null=True, verbose_name='Description texte')
    description2 = HTMLField(blank=True,null=True, verbose_name='Description Tinymce')
    date_ajout =models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
    user_ajout = models.ForeignKey('auth.User',null=True, verbose_name='Ajouté par')
    date_publication = models.DateTimeField(blank=True,null=True,editable=False, verbose_name='Date de publication')

    image_temp = models.ImageField(null=True, blank=True, width_field="image_temp_width", height_field="image_temp_height", upload_to=upload_location)
    image_temp_height = models.IntegerField(default=0)
    image_temp_width = models.IntegerField(default=0)

    def publier(self):
        self.date_publication=timezone.now()
        self.save()

    def is_publie(self):
        return self.date_publication is not None
    is_publie.boolean=True
    is_publie.verbose_name='Est publié ?'

    def __str__(self):
        return self.nom