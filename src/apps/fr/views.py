from django.shortcuts import render, redirect
from apps.fr.models import *
from apps.fr.forms import *
from django.views.generic.base import ContextMixin
from django.views.generic.edit import CreateView
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

class ListMixin(ContextMixin):
	querylist = None
	def get_context_data(self, **kwargs):
	    context = super(ListMixin, self).get_context_data(**kwargs)
	    if self.querylist is None:
	    	context['lista'] = self.model.objects.all()
	    else:	
	    	context['lista'] = self.querylist
			#querylist = model.objects.filter(id__gt = 3)

	    return context
	


class CreateEmpresa(LoginRequiredMixin, ListMixin, CreateView):
	model = Empresa
	form_class = FormEmpresa
	template_name = "fr/empresa.html"
	success_url= reverse_lazy('contacto_empresa')



class CreateEvento(LoginRequiredMixin, ListMixin, CreateView):
	model = Evento
	form_class = FormEvento
	template_name = "fr/evento.html"
	success_url= reverse_lazy('contacto_evento')


class CreateContacto(LoginRequiredMixin, ListMixin, CreateView):
	model = Contacto
	form_class = FormContacto
	template_name = "fr/contacto.html"
	success_url= reverse_lazy('contacto_contactos')




# Create your views here.