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
	nome = "Cardapio"
	context = {'nome':nome}
	return render_to_response('cardapio/index.html', context)

def home(request):
	nome = "Cardapio"
	context = {'nome':nome}
	return render_to_response('cardapio/index.html', context)

