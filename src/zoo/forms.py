from django import forms

from zoo.models import Continente

class ContinenteForm(forms.ModelForm):

	class Meta:
		model= Continente


		fields = [
			'continente',

		]
		labels = {

			'nombre': 'nombre',

		}

		widgets = {

			'nombre': forms.TextInput(atrrs={'class':'form-control'})

		}