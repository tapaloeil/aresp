from django.contrib import admin
from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
	model=Animal
	list_display = ('nom', 'espece','is_publie', 'date_publication', 'date_ajout','user_ajout')
	list_filter = ('espece', 'date_ajout')
	search_fields = ['nom']
	exclude=('user_ajout',)
	fields=(('espece', 'nom'),'date_naissance',('sexe','taille'), ('origine','location'), ('apparence', 'temperament'), 'num_puce','statut', 'description', 'description2',)
	radio_fields={"espece":admin.VERTICAL,"sexe":admin.VERTICAL}

admin.site.register(Animal, AnimalAdmin)
