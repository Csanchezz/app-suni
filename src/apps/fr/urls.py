from django.conf.urls import url
from apps.fr import views

urlpatterns = [
url(r'^empresa/', views.CreateEmpresa.as_view(), name = 'contacto_empresa'),
url(r'^evento/', views.CreateEvento.as_view(), name = 'contacto_evento'),
url(r'^contactos/', views.CreateContacto.as_view(), name = 'contacto_contactos'),
]