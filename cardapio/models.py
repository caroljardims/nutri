from django.db import models

# Create your models here.
class Aux(models.Model):
	tipo = models.IntegerField(max_length=1)
	desc = models.CharField(max_length=4)
	def __unicode__(self):
		return self.desc

class Alimentos(models.Model):
	desc = models.CharField(max_length=20)
	cat_alimento = models.ForeignKey(Aux)
	cor = models.CharField(max_length=10)
	def __unicode__(self):
		return self.desc

class Prepara(models.Model):
	desc = models.CharField(max_length=40)
	inNatura = models.IntegerField(max_length=1)
	enxofre = models.IntegerField(max_length=1)
	cor = models.CharField(max_length=10)
	tipoPrep = models.CharField(max_length=40)
	coccao = models.CharField(max_length=40)
	def __unicode__(self):
		return self.desc

class Prep_Alimentos(models.Model):
	desc = models.CharField(max_length=40)
	alimento = models.ForeignKey(Alimentos)
	prep = models.ForeignKey(Prepara)
	def __unicode__(self):
		return self.desc

class Dia_Cardapio(models.Model):
	dia = models.IntegerField(max_length=2)
	mes = models.IntegerField(max_length=2)
	ano = models.IntegerField(max_length=2)
	def __unicode__(self):
		return self.dia

class Cardapio_Prep(models.Model):
	dia = models.ForeignKey(Dia_Cardapio)
	prep = models.ForeignKey(Prepara)
	r1 = models.IntegerField(max_length=1)
	r2 = models.IntegerField(max_length=1)
	r3_1 = models.IntegerField(max_length=1)
	r3_2 = models.IntegerField(max_length=1)
	r4 = models.IntegerField(max_length=1)
	r5 = models.IntegerField(max_length=1)
	r6 = models.IntegerField(max_length=1)
	r7 = models.IntegerField(max_length=1)
	r8 = models.IntegerField(max_length=1)
	r9 = models.IntegerField(max_length=1)
	r10 = models.IntegerField(max_length=1)
	def __unicode__(self):
		return self.dia.dia