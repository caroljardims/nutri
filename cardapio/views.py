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

