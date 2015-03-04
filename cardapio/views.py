from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from django.forms.models import modelformset_factory
from cardapio.models import *
from cardapio.forms import *

    #############
    #           #
    #   Index   #
    #           #
    #############

def index(request):
	Aux(desc='dsdsds', tipo=1)
	context = {}
	return render_to_response('index.html', context)

def home(request):
	nome = "Cardapio"
	context = {'nome':nome}
	return render_to_response('index.html', context)


    ############################
    #                          #
    #   CRUD Tabela Auxiliar   #
    #                          #
    ############################


def aux(request):
	aux_list = Aux.objects.all()
	context = {'aux_list':aux_list}
	return render_to_response('aux.html', context)

def addaux(request):
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_tipo = request.POST.get('tipo')
		f_desc = request.POST.get('desc')
		auxiliar = Aux(tipo=f_tipo, desc= f_desc)
		auxiliar.save()
		return redirect('/aux')
	context = {'form': form}
	return render(request,"addaux.html", context)

def deleteaux(request,id_aux):
   aux = Aux.objects.get(pk=id_aux).delete()
   context = {'aux':aux}
   return render(request,"delete.html", context)

def editaux(request, id_aux):
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	aux = get_object_or_404(Aux, pk=id_aux)

	if request.method == 'POST':
		f_tipo = request.POST.get('tipo')
		f_desc = request.POST.get('desc')
		
		aux = get_object_or_404(Aux, pk=id_aux)
		if f_tipo: aux.tipo = f_tipo
		if f_desc: aux.desc = f_desc
		aux.save()
		return redirect('/aux')
	context = {'form': form, 'aux':aux}
	return render(request,"editaux.html", context)


    #############################
    #                           #
    #   CRUD Tabela Alimentos   #
    #                           #
    #############################


def alimentos(request):
	al_list = Alimentos.objects.all()
	context = {'al_list':al_list}
	return render_to_response('alimentos.html', context)

def addalimento(request):
	aux_list = Aux.objects.all()
	f = modelformset_factory(Alimentos,AlimentosForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_categoria = request.POST.get('categoria')
		f_desc = request.POST.get('desc')
		f_cor = request.POST.get('cor')
		alimento = Alimentos(cat_alimento_id=f_categoria, desc= f_desc, cor=f_cor)
		alimento.save()
		return redirect('/alimentos')
	context = {'form': form, 'aux_list':aux_list}
	return render(request,"addalimento.html", context)

def veralimento(request, id_alimentos):
	al = get_object_or_404(Alimentos, pk=id_alimentos)
	context = {'al':al}
	return render(request,"veralimento.html", context)

def deletealimento(request,id_alimentos):
   alimento = Alimentos.objects.get(pk=id_alimentos).delete()
   context = {'alimento':alimento}
   return render(request,"delete.html", context)

def editalimento(request, id_alimentos):
	aux_list = Aux.objects.all()
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	al = get_object_or_404(Alimentos, pk=id_alimentos)

	if request.method == 'POST':
		f_categoria = request.POST.get('categoria')
		f_desc = request.POST.get('desc')
		f_cor = request.POST.get('cor')

		al = get_object_or_404(Alimentos, pk=id_alimentos)
		if f_categoria: al.cat_alimento_id = f_categoria
		if f_desc: al.desc = f_desc
		if f_cor: al.cor = f_cor
		al.save()
		return redirect('/alimentos')
	context = {'form': form, 'aux_list':aux_list, 'al':al}
	return render(request,"editalimento.html", context)




	###########################
    #                         #
    #   CRUD Tabela Prepara   #
    #                         #
    ###########################


def prepara(request):
	p_list = Prepara.objects.all()
	aux_list = Aux.objects.all()
	context = {'p_list':p_list,'aux_list':aux_list}
	return render_to_response('prepara.html', context)

def addprepara(request):
	aux_list = Aux.objects.all()
	f = modelformset_factory(Alimentos,AlimentosForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_desc = request.POST.get('desc')
		f_inNatura = request.POST.get('inNatura')
		f_enxofre = request.POST.get('enxofre')
		f_tipo = request.POST.get('tipo')
		f_coccao = request.POST.get('coccao')
		f_cor = request.POST.get('cor')
		prepara = Prepara(desc=f_desc,inNatura=f_inNatura,enxofre=f_enxofre,tipoPrep=f_tipo,coccao=f_coccao,cor=f_cor)
		prepara.save()
		return redirect('/prepara')
	context = {'form': form, 'aux_list':aux_list}
	return render(request,"addprepara.html", context)

def verprepara(request, id_prepara):
	p = get_object_or_404(Prepara, pk=id_prepara)
	context = {'p':p}
	return render(request,"verprepara.html", context)

def deleteprepara(request,id_prepara):
   prepara = Prepara.objects.get(pk=id_prepara).delete()
   context = {'prepara':prepara}
   return render(request,"delete.html", context)

def editprepara(request, id_prepara):
	aux_list = Aux.objects.all()
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	al = get_object_or_404(Prepara, pk=id_prepara)

	if request.method == 'POST':
		f_desc = request.POST.get('desc')
		f_inNatura = request.POST.get('inNatura')
		f_enxofre = request.POST.get('enxofre')
		f_tipo = request.POST.get('tipo')
		f_coccao = request.POST.get('coccao')
		f_cor = request.POST.get('cor')

		al = get_object_or_404(Prepara, pk=id_prepara)
		if f_tipo: al.tipoPrep = f_tipo
		if f_coccao: al.coccao = f_coccao
		if f_inNatura: al.inNatura = f_inNatura
		if f_enxofre: al.enxofre = f_enxofre
		if f_desc: al.desc = f_desc
		if f_cor: al.cor = f_cor
		al.save()
		return redirect('/prepara')
	context = {'form': form, 'aux_list':aux_list, 'al':al}
	return render(request,"editprepara.html", context)

	#############################
    #                           #
    #   Tabela Prep Alimentos   #
    #                           #
    #############################


def prep_alimentos(request,id_prepara):
	al_list = Alimentos.objects.all()
	prep_al_list = Prep_Alimentos.objects.all()
	p = get_object_or_404(Prepara, pk=id_prepara)
	context = {'al_list':al_list,'p':p,'prep_al_list':prep_al_list}
	return render(request,"prep-alimentos.html", context)


















