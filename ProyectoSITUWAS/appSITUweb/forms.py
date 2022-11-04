from django import forms
from .models import Pasajero
from .models import Tarjeta

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen"] 
		#fields = '__all__'

class TarjetaFormulario(forms.ModelForm):
	class Meta:
		model = Tarjeta
		fields=["codigo","monto","idPasajero"] 
		#fields = '__all__'