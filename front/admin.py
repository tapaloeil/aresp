from django.contrib import admin
from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
	list_display = ('nom', 'espece','is_publie', 'date_publication', 'date_ajout','user_ajout')
	list_filter = ('espece', 'date_ajout')
	search_fields = ['nom']
	exclude=('user_ajout',)
	fields=(('espece', 'nom'),'date_naissance',('sexe','taille'), ('origine','location'), ('apparence', 'temperament'), 'num_puce','image_temp','statut', 'description', 'description2',)
	radio_fields={"espece":admin.VERTICAL,"sexe":admin.VERTICAL}
	class Meta:
		model=Animal
		model.is_publie.verbose_name='Est publié ?'
		labels = {'is_publie':'Est publié',}

admin.site.register(Animal, AnimalAdmin)
