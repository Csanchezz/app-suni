from django.shortcuts import render, redirect
from apps.kardex.models import *
from apps.kardex.forms import *
from django.views.generic.edit import CreateView
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
import json



def index(request):
	equipo = Equipo.objects.filter()
	if request.method=='POST':
		formequipo = FormularioEquipo(request.POST or None)
		if formequipo.is_valid():
			new_article = formequipo.save()
		return redirect('kardex_equipo')
	else:
		formequipo = FormularioEquipo()

	context={
		"formequipo": formequipo,
		"equipo_load" : equipo,
	}
	return render(request, 'kardex/index.html', context)


def equipo_entrada(request, id_equipo):
	equipo =  Equipo.objects.get(id = id_equipo)
	lista_entrada = Entrada.objects.filter(equipo = equipo)
	lista_vacia = []
	for ingreso in lista_entrada:
		lista_vacia.append({'id':ingreso.id, 'fecha':str(ingreso.fecha), 'cantidad': ingreso.cantidad, 'observacion':ingreso.observacion})
	return HttpResponse(
			json.dumps({
				"tablainf": lista_vacia,
				})
			)

def equipo_salida(request, id_equipo):
	equipo =  Equipo.objects.get(id = id_equipo)
	lista_salida = Salida.objects.filter(equipo = equipo)
	lista_vacia = []
	for egreso in lista_salida:
		lista_vacia.append({'id':egreso.id, 'fecha':str(egreso.fecha), 'tecnico':str(egreso.tecnico), 'cantidad': egreso.cantidad, 'observacion':egreso.observacion}, )
	return HttpResponse(
			json.dumps({
				"tablainf": lista_vacia,
				})
			)
	


#entrada del equipo
class EntradaCreate(LoginRequiredMixin, CreateView):
	model = Entrada
	form_class = FormularioEntrada
	template_name = "kardex/entrada.html"
	success_url = reverse_lazy('kardex_equipo')

	def form_valid(self, form):
		self.object = form.save(commit = False)
		if self.object.cantidad <= 0:
			return self.form_invalid(form)
		else:
			self.object.save()
			return super(EntradaCreate, self).form_valid(form)


#Salida del equipo
class SalidaCreate(LoginRequiredMixin, CreateView):
	model = Salida
	form_class = FormularioSalida
	template_name = "kardex/salida.html"
	success_url = reverse_lazy('kardex_equipo')

	def form_valid(self, form):
		self.object = form.save(commit = False)
		if self.object.cantidad >  self.object.equipo.existencia:
			return self.form_invalid(form)
		else:
			self.object.save()
			return super(SalidaCreate, self).form_valid(form)




class ProveedorCreate(LoginRequiredMixin, CreateView):
	model = Proveedor
	form_class = FormularioProveedor
	template_name = "kardex/proveedor.html"