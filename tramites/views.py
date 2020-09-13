from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import *
from .models import *
from django.views.generic import CreateView
from django.urls import reverse
from .forms import TramiteForm
# Create your views here.


class IndexView(ListView):
    template_name = 'tramites/index.html'
    context_object_name = 'mensaje'
    #queryset = Personaje.objects.all()
    #serializer_class = DeporteSerializer

    def get_queryset(self):
        return "Pagina inicial"

class TramitesView(CreateView):
    model = Tramite
    template_name = "tramites/registrarTramite.html"
    form_class = TramiteForm
    #success_url = reverse('konexbvc:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TramitesView, self).form_valid(form)

