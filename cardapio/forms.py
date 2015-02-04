from django import forms
from django.forms import ModelForm
from cardapio.models import *

class AuxForm(ModelForm):
    class Meta:
	model = Aux
	fields = '__all__'
	
class PreparaForm(ModelForm):
    class Meta:
	model = Prepara
	fields = '__all__'

class AlimentosForm(ModelForm):
    class Meta:
	model = Alimentos
	fields = '__all__'

class PrepAlimentosForm(ModelForm):
    class Meta:
	model = Prep_Alimentos
	fields = '__all__'