from django.views.generic import ListView, TemplateView, DetailView
from .models import Angebot
# Create your views here.


class HomeView(TemplateView):
    template_name = "kartenwerk/index.html"


class AngebotList(ListView):
    model = Angebot
    template_name = "kartenwerk/angebote.html"
    context_object_name = "angebote"


class AngebotDetail(DetailView):
    model = Angebot
    template_name = 'kartenwerk/angebot_detail.html'


class ReferenzenView(TemplateView):
    template_name = "kartenwerk/referenzen.html"


class AboutView(TemplateView):
    template_name = "kartenwerk/about.html"
