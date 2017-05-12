from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
	class Meta:
		model=Animal
		fields = ('espece', 'sexe', 'nom', 'date_naissance', 'taille', 'origine', 'location', 'apparence', 'temperament', 'num_puce', 'statut', 'description','image_temp',)